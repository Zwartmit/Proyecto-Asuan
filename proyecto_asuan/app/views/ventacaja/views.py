import django
from django.contrib.auth.decorators import login_required
import os
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect

from app.models import VentaCaja
from app.forms import VentaCajaForm

def lista_ventacaja(request):
    nombre = {
        'titulo': 'Caja',
        'ventaas': VentaCaja.objects.all()
    }
    return render(request, 'ventacaja/listar.html',nombre)

###### LISTAR ######

class VentaCajaListView(ListView):
    model = VentaCaja
    template_name = 'ventacaja/listar.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'Juan'}
        return JsonResponse(nombre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de ventas de caja'
        context['entidad'] = 'Listado de ventas decaja'
        context['listar_url'] = reverse_lazy('app:ventacaja_lista')
        context['crear_url'] = reverse_lazy('app:ventacaja_crear')
        return context

###### CREAR ######

class VentaCajaCreateView(CreateView):
    model = VentaCaja
    form_class = VentaCajaForm
    template_name = 'ventacaja/crear.html'
    success_url = reverse_lazy('app:ventacaja_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Agregar venta de caja'
        context['entidad'] = 'Agregar venta de caja'
        context['error'] = 'Esta venta ya existe'
        context['listar_url'] = reverse_lazy('app:ventacaja_lista')
        return context
    
###### EDITAR ######

class VentaCajaUpdateView(UpdateView):
    model = VentaCajaForm
    form_class = VentaCajaForm
    template_name = 'ventacaja/crear.html'
    success_url = reverse_lazy('app:ventacaja_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar venta de caja'
        context['entidad'] = 'Editar venta de caja'
        context['error'] = 'Esta venta ya existe'
        context['listar_url'] = reverse_lazy('app:venta_lista')
        return context
    
###### ELIMINAR ######

class VentaCajaDeleteView(DeleteView):
    model = VentaCaja
    template_name = 'ventacaja/eliminar.html'
    success_url = reverse_lazy('app:ventacaja_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar venta de caja'
        context['entidad'] = 'Eliminar venta de caja'
        context['listar_url'] = reverse_lazy('app:ventacaja_lista')
        return context 
    
    