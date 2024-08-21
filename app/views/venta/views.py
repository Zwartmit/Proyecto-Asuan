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
from django.db.models import Q
from app.models import Venta, Producto
from app.forms import VentaForm, ClienteForm, DetalleVentaForm

from app.models import Venta
from app.forms import VentaForm

@method_decorator(never_cache, name='dispatch')
def lista_venta(request):
    nombre = {
        'titulo': 'Listado de ventas',
        'ventaas': Venta.objects.all()
    }
    return render(request, 'venta/listar.html',nombre)

###### LISTAR ######

@method_decorator(never_cache, name='dispatch')
class VentaListView(ListView):
    model = Venta
    template_name = 'venta/listar.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'Juan'}
        return JsonResponse(nombre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de ventas'
        context['entidad'] = 'Listado de ventas'
        context['listar_url'] = reverse_lazy('app:venta_lista')
        context['crear_url'] = reverse_lazy('app:venta_crear')
        return context

###### API ######
    
def productos_api(request):
    term = request.GET.get('term', '') 
    productos = Producto.objects.filter(Q(producto__icontains=term)).values('id', 'producto', 'valor')
    return JsonResponse(list(productos), safe=False)

###### CREAR ######

@method_decorator(never_cache, name='dispatch')
class VentaCreateView(CreateView):
    model = Venta
    form_class = VentaForm
    template_name = 'venta/crear.html'
    success_url = reverse_lazy('app:venta_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registrar venta'
        context['entidad'] = 'Registrar venta'
        context['error'] = 'Esta venta ya existe'
        context['listar_url'] = reverse_lazy('app:venta_lista')
        context['cliente_form'] = ClienteForm()
        context['venta_form'] = VentaForm()
        context['detalleventa_form'] = DetalleVentaForm()
        return context
    
###### EDITAR ######

@method_decorator(never_cache, name='dispatch')
class VentaUpdateView(UpdateView):
    model = Venta
    form_class = VentaForm
    template_name = 'venta/crear.html'
    success_url = reverse_lazy('app:venta_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar venta'
        context['entidad'] = 'Editar venta'
        context['error'] = 'Esta venta ya existe'
        context['listar_url'] = reverse_lazy('app:venta_lista')
        return context
    
###### ELIMINAR ######

@method_decorator(never_cache, name='dispatch')
class VentaDeleteView(DeleteView):
    model = Venta
    template_name = 'venta/eliminar.html'
    success_url = reverse_lazy('app:venta_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar venta'
        context['entidad'] = 'Eliminar venta'
        context['listar_url'] = reverse_lazy('app:venta_lista')
        return context 
    
def ventas_view(request):
    return render(request, 'venta/ventas.html')