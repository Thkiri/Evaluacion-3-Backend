from io import BytesIO
from urllib.error import URLError
from urllib.request import Request, urlopen

from django import forms
from django.core.files.base import ContentFile
from PIL import Image, UnidentifiedImageError

from .models import Libro


class LibroForm(forms.ModelForm):
    portada_url = forms.URLField(
        required=False,
        label='URL de portada (opcional)',
        help_text='Pega el enlace directo de una imagen para guardarla automáticamente como portada.',
        widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://ejemplo.com/portada.jpg'}),
    )

    class Meta:
        model = Libro
        fields = [
            'categoria',
            'titulo',
            'autor',
            'isbn',
            'stock',
            'precio_arriendo',
            'fecha_publicacion',
            'disponible',
            'portada',
        ]
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del libro'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del autor'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 9780307474728'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'precio_arriendo': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
            'fecha_publicacion': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'},
                format='%Y-%m-%d',
            ),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'portada': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_precio_arriendo(self):
        precio = self.cleaned_data.get('precio_arriendo')
        if precio is not None and precio < 0:
            raise forms.ValidationError('El precio de arriendo no puede ser negativo.')
        return precio

    def clean(self):
        cleaned_data = super().clean()
        self._downloaded_cover = None
        url = cleaned_data.get('portada_url')
        uploaded_file = self.files.get('portada')

        if url and not uploaded_file:
            try:
                req = Request(url, headers={'User-Agent': 'BiblioTech/1.0'})
                with urlopen(req, timeout=10) as resp:
                    data = resp.read()
                img = Image.open(BytesIO(data))
                img.verify()
                ext = (img.format or 'JPEG').lower()
                if ext == 'jpeg':
                    ext = 'jpg'
                isbn = cleaned_data.get('isbn') or 'portada'
                self._downloaded_cover = (f'{isbn}.{ext}', data)
            except (URLError, TimeoutError, ValueError, UnidentifiedImageError, OSError):
                self.add_error('portada_url', 'No se pudo descargar una imagen válida desde esa URL.')

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        if getattr(self, '_downloaded_cover', None):
            filename, data = self._downloaded_cover
            instance.portada.save(filename, ContentFile(data), save=False)
        if commit:
            instance.save()
        return instance
