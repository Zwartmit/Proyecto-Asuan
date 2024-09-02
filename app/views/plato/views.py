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

from app.models import Plato
from app.forms import PlatoForm

@method_decorator(never_cache, name='dispatch')
def lista_platos(request):
    nombre = {
        'titulo': 'Listado de platos',
        'platos': Plato.objects.all()
    }
    return render(request, 'plato/listar.html',nombre)

###### LISTAR ######

@method_decorator(never_cache, name='dispatch')
class PlatoListView(ListView):
    model = Plato
    template_name = 'plato/listar.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'Juan'}
        return JsonResponse(nombre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de platos'
        context['entidad'] = 'Listado de platos'
        context['listar_url'] = reverse_lazy('app:plato_lista')
        context['crear_url'] = reverse_lazy('app:plato_crear')
        return context

###### CREAR ######

@method_decorator(never_cache, name='dispatch')
class PlatoCreateView(CreateView):
    model = Plato
    form_class = PlatoForm
    template_name = 'plato/crear.html'
    success_url = reverse_lazy('app:plato_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registrar plato'
        context['entidad'] = 'Registrar plato'
        context['error'] = 'Este plato ya existe'
        context['listar_url'] = reverse_lazy('app:plato_lista')
        return context
    
    def form_valid(self, form):
        plato = form.cleaned_data.get('plato').lower()
        
        if Plato.objects.filter(plato__iexact=plato).exists():
            form.add_error('plato', 'Ya existe un plato con este nombre.')
            return self.form_invalid(form)
        
        return super().form_valid(form)
    
###### EDITAR ######

@method_decorator(never_cache, name='dispatch')
class PlatoUpdateView(UpdateView):
    model = Plato
    form_class = PlatoForm
    template_name = 'plato/crear.html'
    success_url = reverse_lazy('app:plato_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar plato'
        context['entidad'] = 'Editar plato'
        context['error'] = 'Este plato ya existe'
        context['listar_url'] = reverse_lazy('app:plato_lista')
        return context
    
###### ELIMINAR ######

@method_decorator(never_cache, name='dispatch')
class PlatoDeleteView(DeleteView):
    model = Plato
    template_name = 'plato/eliminar.html'
    success_url = reverse_lazy('app:plato_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar plato'
        context['entidad'] = 'Eliminar plato'
        context['listar_url'] = reverse_lazy('app:plato_lista')
        return context
