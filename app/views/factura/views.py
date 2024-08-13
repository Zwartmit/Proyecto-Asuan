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

from app.models import Factura
from app.forms import FacturaForm

@method_decorator(never_cache, name='dispatch')
def lista_factura(request):
    nombre = {
        'titulo': 'Listado de facturas',
        'facturas': Factura.objects.all()
    }
    return render(request, 'factura/listar.html',nombre)

###### LISTAR ######

@method_decorator(never_cache, name='dispatch')
class FacturaListView(ListView):
    model = Factura
    template_name = 'factura/listar.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'Juan'}
        return JsonResponse(nombre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de facturas'
        context['entidad'] = 'Listado de facturas'
        context['listar_url'] = reverse_lazy('app:factura_lista')
        context['crear_url'] = reverse_lazy('app:factura_crear')
        return context

###### CREAR ######

@method_decorator(never_cache, name='dispatch')
class FacturaCreateView(CreateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'factura/crear.html'
    success_url = reverse_lazy('app:factura_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registrar factura'
        context['entidad'] = 'Registrar factura'
        context['error'] = 'Esta factura ya existe'
        context['listar_url'] = reverse_lazy('app:factura_lista')
        return context
    
    def form_valid(self, form):
        factura = form.cleaned_data.get('factura').lower()
        
        if Factura.objects.filter(factura__iexact=factura).exists():
            form.add_error('factura', 'Ya existe una factura con este id.')
            return self.form_invalid(form)
        return super().form_valid(form)
    
###### EDITAR ######

@method_decorator(never_cache, name='dispatch')
class FacturaUpdateView(UpdateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'factura/crear.html'
    success_url = reverse_lazy('app:factura_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar factura'
        context['entidad'] = 'Editar factura'
        context['error'] = 'Esta factura ya existe'
        context['listar_url'] = reverse_lazy('app:factura_lista')
        return context
    
    def form_valid(self, form):
        factura = form.cleaned_data.get('factura').lower()
        
        if Factura.objects.filter(factura__iexact=factura).exists():
            form.add_error('factura', 'Ya existe una factura con este id.')
            return self.form_invalid(form)
        return super().form_valid(form)
    
###### ELIMINAR ######

@method_decorator(never_cache, name='dispatch')
class FacturaDeleteView(DeleteView):
    model = Factura
    template_name = 'factura/eliminar.html'
    success_url = reverse_lazy('app:factura_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar factura'
        context['entidad'] = 'Eliminar factura'
        context['listar_url'] = reverse_lazy('app:factura_lista')
        return context
    
    