from django.contrib import admin
from .models import Categoria, Libro

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nombre', 'activo')
    list_filter = ('activo',)
    search_fields = ('nombre', 'codigo')
    ordering = ('nombre',)


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'categoria', 'precio_arriendo', 'stock', 'fecha_publicacion', 'disponible')
    list_filter = ('categoria', 'disponible', 'fecha_publicacion')
    search_fields = ('titulo', 'autor', 'isbn')
    list_select_related = ('categoria',)
    ordering = ('-id',)
