from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.core.exceptions import ValidationError
from app.models import Administrador
from app.forms import AdministradorForm

@method_decorator(login_required, name='dispatch')
class AdministradorListView(ListView):
    model = Administrador
    template_name = 'administrador/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de administradores'
        context['entidad'] = 'Listado de administradores'
        context['listar_url'] = reverse_lazy('app:administrador_lista')
        context['crear_url'] = reverse_lazy('app:administrador_crear')
        context['has_permission'] = self.request.user.has_perm('app.view_administrador')

        if self.request.user.groups.filter(name='Operador').exists():
            context['can_add'] = False
        else:
            context['can_add'] = self.request.user.has_perm('app.add_administrador')

        return context

@method_decorator(login_required, name='dispatch')
class AdministradorCreateView(CreateView):
    model = Administrador
    form_class = AdministradorForm
    template_name = 'administrador/crear.html'
    success_url = reverse_lazy('app:administrador_lista')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registrar administrador'
        context['entidad'] = 'Registrar administrador'
        context['listar_url'] = reverse_lazy('app:administrador_lista')
        context['has_permission'] = not self.request.user.groups.filter(name='Operador').exists() and self.request.user.has_perm('app.add_administrador')
        return context

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.has_perm('app.add_administrador') or self.request.user.groups.filter(name='Operador').exists():
            list_context = AdministradorListView.as_view()(request, *args, **kwargs).context_data
            return render(request, 'administrador/listar.html', list_context)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ValidationError as e:
            form.add_error(None, e)
            return self.form_invalid(form)

@method_decorator(login_required, name='dispatch')
class AdministradorUpdateView(UpdateView):
    model = Administrador
    form_class = AdministradorForm
    template_name = 'administrador/crear.html'
    success_url = reverse_lazy('app:administrador_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar administrador'
        context['entidad'] = 'Editar administrador'
        context['listar_url'] = reverse_lazy('app:administrador_lista')
        context['has_permission'] = not self.request.user.groups.filter(name='Operador').exists() and self.request.user.has_perm('app.change_administrador')
        return context

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.has_perm('app.change_administrador') or self.request.user.groups.filter(name='Operador').exists():
            list_context = AdministradorListView.as_view()(request, *args, **kwargs).context_data
            return render(request, 'administrador/listar.html', list_context)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ValidationError as e:
            form.add_error(None, e)
            return self.form_invalid(form)

@method_decorator(login_required, name='dispatch')
class AdministradorDeleteView(DeleteView):
    model = Administrador
    template_name = 'administrador/eliminar.html'
    success_url = reverse_lazy('app:administrador_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar administrador'
        context['entidad'] = 'Eliminar administrador'
        context['listar_url'] = reverse_lazy('app:administrador_lista')
        context['has_permission'] = not self.request.user.groups.filter(name='Operador').exists() and self.request.user.has_perm('app.delete_administrador')
        return context

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.has_perm('app.delete_administrador') or self.request.user.groups.filter(name='Operador').exists():
            list_context = AdministradorListView.as_view()(request, *args, **kwargs).context_data
            return render(request, 'administrador/listar.html', list_context)
        return super().dispatch(request, *args, **kwargs)
