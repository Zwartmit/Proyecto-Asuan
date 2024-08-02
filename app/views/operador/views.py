from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from app.models import Operador
from app.forms import OperadorForm

@method_decorator(login_required, name='dispatch')
class OperadorListView(ListView):
    model = Operador
    template_name = 'operador/listar.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('app.view_operador'):
            return JsonResponse({'error': 'No tienes permiso para ver esta página'}, status=403)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de operadores'
        context['entidad'] = 'Listado de operadores'
        context['listar_url'] = reverse_lazy('app:operador_lista')
        context['crear_url'] = reverse_lazy('app:operador_crear')
        return context

@method_decorator(login_required, name='dispatch')
class OperadorCreateView(CreateView):
    model = Operador
    form_class = OperadorForm
    template_name = 'operador/crear.html'
    success_url = reverse_lazy('app:operador_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('app.add_operador'):
            return JsonResponse({'error': 'No tienes permiso para crear un operador'}, status=403)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registrar operador'
        context['entidad'] = 'Registrar operador'
        context['listar_url'] = reverse_lazy('app:operador_lista')
        return context

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

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('app.change_operador'):
            return JsonResponse({'error': 'No tienes permiso para editar este operador'}, status=403)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar operador'
        context['entidad'] = 'Editar operador'
        context['listar_url'] = reverse_lazy('app:operador_lista')
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class OperadorDeleteView(DeleteView):
    model = Operador
    template_name = 'operador/eliminar.html'
    success_url = reverse_lazy('app:operador_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('app.delete_operador'):
            return JsonResponse({'error': 'No tienes permiso para eliminar este operador'}, status=403)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar operador'
        context['entidad'] = 'Eliminar operador'
        context['listar_url'] = reverse_lazy('app:operador_lista')
        return context
