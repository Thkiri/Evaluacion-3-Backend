from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from .forms import LibroForm
from .models import Libro


class LibroListView(ListView):

    model = Libro
    queryset = Libro.objects.select_related('categoria')
    template_name = 'libros/libro_list.html'
    context_object_name = 'libros'


class LibroDetailView(DetailView):

    model = Libro
    queryset = Libro.objects.select_related('categoria')
    template_name = 'libros/libro_detail.html'
    context_object_name = 'libro'


class LibroCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    model = Libro
    form_class = LibroForm
    template_name = 'libros/libro_form.html'
    success_url = reverse_lazy('libros:lista')
    success_message = "Libro creado correctamente."


class LibroUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Libro
    form_class = LibroForm
    template_name = 'libros/libro_form.html'
    success_url = reverse_lazy('libros:lista')
    success_message = "Libro actualizado correctamente."


class LibroDeleteView(LoginRequiredMixin, DeleteView):

    model = Libro
    template_name = 'libros/libro_confirm_delete.html'
    context_object_name = 'libro'
    success_url = reverse_lazy('libros:lista')

    def form_valid(self, form):
        messages.success(self.request, "Libro eliminado correctamente.")
        return super().form_valid(form)
