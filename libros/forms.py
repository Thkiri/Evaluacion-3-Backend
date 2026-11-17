from django import forms
from .models import Libro


class LibroForm(forms.ModelForm):
    
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
