from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.core.exceptions import ValidationError
from app.models import Operador
from app.forms import OperadorForm

@method_decorator(login_required, name='dispatch')
class OperadorListView(ListView):
    model = Operador
    template_name = 'operador/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de operadores'
        context['entidad'] = 'Listado de operadores'
        context['listar_url'] = reverse_lazy('app:operador_lista')
        context['crear_url'] = reverse_lazy('app:operador_crear')
        context['has_permission'] = self.request.user.has_perm('app.view_operador')

        if self.request.user.groups.filter(name='Operador').exists():
            context['can_add'] = False
        else:
            context['can_add'] = self.request.user.has_perm('app.add_operador')

        return context

@method_decorator(login_required, name='dispatch')
class OperadorCreateView(CreateView):
    model = Operador
    form_class = OperadorForm
    template_name = 'operador/crear.html'
    success_url = reverse_lazy('app:operador_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registrar operador'
        context['entidad'] = 'Registrar operador'
        context['listar_url'] = reverse_lazy('app:operador_lista')
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Operador').exists() or not request.user.has_perm('app.add_operador'):
            context = self.get_context_data()
            context['has_permission'] = False
            return render(request, 'operador/listar.html', context)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ValidationError as e:
            form.add_error(None, e)
            return self.form_invalid(form)

@method_decorator(login_required, name='dispatch')
class OperadorUpdateView(UpdateView):
    model = Operador
    form_class = OperadorForm
    template_name = 'operador/crear.html'
    success_url = reverse_lazy('app:operador_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar operador'
        context['entidad'] = 'Editar operador'
        context['listar_url'] = reverse_lazy('app:operador_lista')
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Operador').exists() or not request.user.has_perm('app.change_operador'):
            context = self.get_context_data()
            context['has_permission'] = False
            return render(request, 'operador/listar.html', context)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ValidationError as e:
            form.add_error(None, e)
            return self.form_invalid(form)

@method_decorator(login_required, name='dispatch')
class OperadorDeleteView(DeleteView):
    model = Operador
    template_name = 'operador/eliminar.html'
    success_url = reverse_lazy('app:operador_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar operador'
        context['entidad'] = 'Eliminar operador'
        context['listar_url'] = reverse_lazy('app:operador_lista')
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Operador').exists() or not request.user.has_perm('app.delete_operador'):
            context = self.get_context_data()
            context['has_permission'] = False
            return render(request, 'operador/listar.html', context)
        return super().dispatch(request, *args, **kwargs)
