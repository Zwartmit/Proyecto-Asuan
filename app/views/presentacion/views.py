import django
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
import os
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect

from app.models import Presentacion
from app.forms import PresentacionForm

@method_decorator(never_cache, name='dispatch')
def lista_presentacion(request):
    nombre = {
        'titulo': 'Listado de presentaciones',
        'presentaciones': Presentacion.objects.all()
    }
    return render(request, 'presentacion/listar.html',nombre)

###### LISTAR ######

@method_decorator(never_cache, name='dispatch')
class PresentacionListView(ListView):
    model = Presentacion
    template_name = 'presentacion/listar.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'Juan'}
        return JsonResponse(nombre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de presentaciones'
        context['entidad'] = 'Listado de presentaciones'
        context['listar_url'] = reverse_lazy('app:presentacion_lista')
        context['crear_url'] = reverse_lazy('app:presentacion_crear')
        return context

###### CREAR ######

@method_decorator(never_cache, name='dispatch')
class PresentacionCreateView(CreateView):
    model = Presentacion
    form_class = PresentacionForm
    template_name = 'presentacion/crear.html'
    success_url = reverse_lazy('app:presentacion_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registrar presentación'
        context['entidad'] = 'Registrar presentación'
        context['error'] = 'Esta presentación ya existe'
        context['listar_url'] = reverse_lazy('app:presentacion_lista')
        return context
    
    def form_valid(self, form):
        presentacion = form.cleaned_data.get('presentacion').lower()
        
        if Presentacion.objects.filter(presentacion__iexact=presentacion).exists():
            form.add_error('presentacion', 'Ya existe una presentación con este nombre.')
            return self.form_invalid(form)
        
        return super().form_valid(form)
    
###### EDITAR ######

@method_decorator(never_cache, name='dispatch')
class PresentacionUpdateView(UpdateView):
    model = Presentacion
    form_class = PresentacionForm
    template_name = 'presentacion/crear.html'
    success_url = reverse_lazy('app:presentacion_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar presentación'
        context['entidad'] = 'Editar presentación'
        context['error'] = 'Esta presentación ya existe'
        context['listar_url'] = reverse_lazy('app:presentacion_lista')
        return context
    
###### ELIMINAR ######

@method_decorator(never_cache, name='dispatch')
class PresentacionDeleteView(DeleteView):
    model = Presentacion
    template_name = 'presentacion/eliminar.html'
    success_url = reverse_lazy('app:presentacion_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar presentación'
        context['entidad'] = 'Eliminar presentación'
        context['listar_url'] = reverse_lazy('app:presentacion_lista')
        return context
