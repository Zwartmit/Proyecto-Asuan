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

from app.models import Mesero
from app.forms import MeseroForm

@method_decorator(never_cache, name='dispatch')
def lista_mesero(request):
    nombre = {
        'titulo': 'Listado de meseros',
        'meseros': Mesero.objects.all()
    }
    return render(request, 'mesero/listar.html',nombre)

###### LISTAR ######

@method_decorator(never_cache, name='dispatch')
class MeseroListView(ListView):
    model = Mesero
    template_name = 'mesero/listar.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'Juan'}
        return JsonResponse(nombre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de meseros'
        context['entidad'] = 'Listado de meseros'
        context['listar_url'] = reverse_lazy('app:mesero_lista')
        context['crear_url'] = reverse_lazy('app:mesero_crear')
        return context

###### CREAR ######

@method_decorator(never_cache, name='dispatch')
class MeseroCreateView(CreateView):
    model = Mesero
    form_class = MeseroForm
    template_name = 'mesero/crear.html'
    success_url = reverse_lazy('app:mesero_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registrar mesero'
        context['entidad'] = 'Registrar mesero'
        context['error'] = 'Este mesero ya existe'
        context['listar_url'] = reverse_lazy('app:mesero_lista')
        return context
    
###### EDITAR ######

@method_decorator(never_cache, name='dispatch')
class MeseroUpdateView(UpdateView):
    model = Mesero
    form_class = MeseroForm
    template_name = 'mesero/crear.html'
    success_url = reverse_lazy('app:mesero_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar mesero'
        context['entidad'] = 'Editar mesero'
        context['error'] = 'Esta mesero ya existe'
        context['listar_url'] = reverse_lazy('app:mesero_lista')
        return context

###### ELIMINAR ######

@method_decorator(never_cache, name='dispatch')
class MeseroDeleteView(DeleteView):
    model = Mesero
    template_name = 'mesero/eliminar.html'
    success_url = reverse_lazy('app:mesero_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar mesero'
        context['entidad'] = 'Eliminar mesero'
        context['listar_url'] = reverse_lazy('app:mesero_lista')
        return context
