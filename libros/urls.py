from django.urls import path
from .views import (
    LibroCreateView,
    LibroDeleteView,
    LibroDetailView,
    LibroListView,
    LibroUpdateView,
)

app_name = 'libros'

urlpatterns = [
    path('', LibroListView.as_view(), name='lista'),
    path('libro/<int:pk>/', LibroDetailView.as_view(), name='detalle'),
    path('libro/nuevo/', LibroCreateView.as_view(), name='crear'),
    path('libro/<int:pk>/editar/', LibroUpdateView.as_view(), name='editar'),
    path('libro/<int:pk>/eliminar/', LibroDeleteView.as_view(), name='eliminar'),
]
