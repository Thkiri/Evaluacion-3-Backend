from django.db import models

class Categoria(models.Model):
    """
    Modelo Padre (Clasificador): Categoria
    Gestionado exclusivamente desde el panel de Django Admin.
    """
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
    codigo = models.CharField(max_length=20, unique=True, verbose_name="Código")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    activo = models.BooleanField(default=True, verbose_name="Estado Activo")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Libro(models.Model):
    """
    Modelo Hijo (Operativo): Libro
    Posee ForeignKey hacia Categoria y al menos 4 tipos de campos:
    texto (titulo, autor, isbn), numérico/decimal (stock, precio_arriendo),
    fecha (fecha_publicacion) y booleano (disponible), más imagen (portada).
    """
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='libros',
        verbose_name="Categoría"
    )
    titulo = models.CharField(max_length=200, verbose_name="Título")
    autor = models.CharField(max_length=150, verbose_name="Autor")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN")
    stock = models.PositiveIntegerField(default=1, verbose_name="Stock")
    precio_arriendo = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Precio de Arriendo"
    )
    fecha_publicacion = models.DateField(verbose_name="Fecha de Publicación")
    disponible = models.BooleanField(default=True, verbose_name="Disponible para arriendo")
    portada = models.ImageField(
        upload_to='portadas/',
        blank=True,
        null=True,
        verbose_name="Portada"
    )

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ['-id']

    def __str__(self):
        return f"{self.titulo} ({self.autor})"
