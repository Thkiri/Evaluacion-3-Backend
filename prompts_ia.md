# Bitácora de Inteligencia Artificial (Hito 3 - BiblioTech)

Asistente de ia utilizado Gemini 4 Hydrogen

promt 1 diseño del frontend en DTL y Bootstrap 5.

Rol: Actua como un desarrollador front end senior especializado en django template, diseño responsivo y boostrap 5
tarea: diseña una plantilla base modular 'templates/base.html' y las plantillas de ciclo CRUD ('libro_list.html', 'libro_detail.html', 'libro_form.html' y 'libro_confirm_delete.html')
contexto: el backend esta construido en django con la app 'libros' un modelo 'Categoria' gestionado exclusivamente desde Django Admin y un modelo 'Libro' (categoria, titulo, autor, isbn, stock, precio_arriendo, fecha_publicacion, disponible y portada como ImageField). Las vistas son CBVs ('LibroListView' optimizada con 'select_related('categoria')', 'LibroDetailView', 'LibroCreateView', 'LibroUpdateView' y 'LibroDeleteView') registradas bajo el namespace 'libros' (lista, detalle, crear, editar, eliminar').

formato plantillas HTML5 válidas usando herencia DTL ('{% extends 'base.html %}' y '{% block content %}').
Bootstrap 5 cargado mediante CDN en 'base.html', con barra de navegación superior, contenedor principal y pie de página limpio.
Grilla responsive (row-cols-*) con tarjetas ('card') en 'libro_list.html', mostrando la portada ('libro.portada.url') con un respaldo visual cuando el libro no tenga imagen cargada, además de badges para disponibilidad y categoría.
formulario en 'libro_form.html' con method="post", enctype="multipart/form-data" para soportar 'ImageField','{% csrf_token %}' y renderizado ordenado de errores de validación por campo.
confirmación explícita de borrado en 'libro_confirm_delete.html' con botones diferenciados para confirmar ('POST') o cancelar.





promt 2

Rol: 
Tarea: 
Contexto:
Formato:
