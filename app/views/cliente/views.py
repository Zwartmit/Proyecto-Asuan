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

from app.models import Cliente
from app.forms import ClienteForm

@method_decorator(never_cache, name='dispatch')
def lista_cliente(request):
    nombre = {
        'titulo': 'Listado de clientes',
        'cliente': Cliente.objects.all()
    }
    return render(request, 'cliente/listar.html',nombre)

###### LISTAR ######

@method_decorator(never_cache, name='dispatch')
class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente/listar.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'Juan'}
        return JsonResponse(nombre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de clientes'
        context['entidad'] = 'Listado de clientes'
        context['listar_url'] = reverse_lazy('app:cliente_lista')
        context['crear_url'] = reverse_lazy('app:cliente_crear')
        return context

###### CREAR ######

@method_decorator(never_cache, name='dispatch')
class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/crear.html'
    success_url = reverse_lazy('app:cliente_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form() 
        context['titulo'] = 'Registrar cliente'
        context['entidad'] = 'Registrar cliente'
        context['error'] = 'Este cliente ya está registrado'
        context['listar_url'] = reverse_lazy('app:cliente_lista')
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            return JsonResponse({'success': True}, status=200)
        return response

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        return super().form_invalid(form)
    
###### EDITAR ######

@method_decorator(never_cache, name='dispatch')
class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/crear.html'
    success_url = reverse_lazy('app:cliente_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar cliente'
        context['entidad'] = 'Editar cliente'
        context['error'] = 'Este cliente ya está registrad'
        context['listar_url'] = reverse_lazy('app:cliente_lista')
        return context

###### ELIMINAR ######

@method_decorator(never_cache, name='dispatch')
class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente/eliminar.html'
    success_url = reverse_lazy('app:cliente_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar cliente'
        context['entidad'] = 'Eliminar cliente'
        context['listar_url'] = reverse_lazy('app:cliente_lista')
        return context
