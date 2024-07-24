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

from app.models import Cuenta
from app.forms import CuentaForm

@method_decorator(never_cache, name='dispatch')
def lista_cuenta(request):
    nombre = {
        'titulo': 'Listado de cuentas',
        'cuentas': Cuenta.objects.all()
    }
    return render(request, 'cuenta/listar.html',nombre)

###### LISTAR ######

@method_decorator(never_cache, name='dispatch')
class CuentaListView(ListView):
    model = Cuenta
    template_name = 'cuenta/listar.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'Juan'}
        return JsonResponse(nombre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de cuentas'
        context['entidad'] = 'Listado de cuentas'
        context['listar_url'] = reverse_lazy('app:cuenta_lista')
        context['crear_url'] = reverse_lazy('app:cuenta_crear')
        return context

###### CREAR ######

@method_decorator(never_cache, name='dispatch')
class CuentaCreateView(CreateView):
    model = Cuenta
    form_class = CuentaForm
    template_name = 'cuenta/crear.html'
    success_url = reverse_lazy('app:cuenta_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registrar cuenta'
        context['entidad'] = 'Registrar cuenta'
        context['error'] = 'Esta cuenta ya existe'
        context['listar_url'] = reverse_lazy('app:cuenta_lista')
        return context
    
###### EDITAR ######

@method_decorator(never_cache, name='dispatch')
class CuentaUpdateView(UpdateView):
    model = Cuenta
    form_class = CuentaForm
    template_name = 'cuenta/crear.html'
    success_url = reverse_lazy('app:cuenta_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar cuenta'
        context['entidad'] = 'Editar cuenta'
        context['error'] = 'Esta cuenta ya existe'
        context['listar_url'] = reverse_lazy('app:cuenta_lista')
        return context
    
###### ELIMINAR ######

@method_decorator(never_cache, name='dispatch')
class CuentaDeleteView(DeleteView):
    model = Cuenta
    template_name = 'cuenta/eliminar.html'
    success_url = reverse_lazy('app:cuenta_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar cuenta'
        context['entidad'] = 'Eliminar cuenta'
        context['listar_url'] = reverse_lazy('app:cuenta_lista')
        return context
