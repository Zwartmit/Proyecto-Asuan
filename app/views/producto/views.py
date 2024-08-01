from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.views.decorators.cache import never_cache
from app.models import Producto
from app.forms import ProductoForm

@method_decorator(never_cache, name='dispatch')
class ProductoListView(ListView):
    model = Producto
    template_name = 'producto/listar.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'No autenticado'}, status=403)
        if not request.user.has_perm('app.view_producto'):
            return JsonResponse({'error': 'No tienes permiso para ver esta página'}, status=403)
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'Juan'}
        return JsonResponse(nombre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de productos'
        context['entidad'] = 'Listado de productos'
        context['listar_url'] = reverse_lazy('app:producto_lista')
        context['crear_url'] = reverse_lazy('app:producto_crear')
        return context

@method_decorator(never_cache, name='dispatch')
class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/crear.html'
    success_url = reverse_lazy('app:producto_lista')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'No autenticado'}, status=403)
        if not request.user.has_perm('app.add_producto'):
            return JsonResponse({'error': 'No tienes permiso para crear un producto'}, status=403)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registrar producto'
        context['entidad'] = 'Registrar producto'
        context['error'] = 'Este producto ya existe'
        context['listar_url'] = reverse_lazy('app:producto_lista')
        return context

    def form_valid(self, form):
        producto = form.cleaned_data.get('producto').lower()
        if Producto.objects.filter(producto__iexact=producto).exists():
            form.add_error('producto', 'Ya existe un producto con este nombre.')
            return self.form_invalid(form)
        messages.success(self.request, 'Producto creado exitosamente')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Ocurrió un error al crear el producto')
        return super().form_invalid(form)

@method_decorator(never_cache, name='dispatch')
class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/crear.html'
    success_url = reverse_lazy('app:producto_lista')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'No autenticado'}, status=403)
        if not request.user.has_perm('app.change_producto'):
            return JsonResponse({'error': 'No tienes permiso para editar este producto'}, status=403)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar producto'
        context['entidad'] = 'Editar producto'
        context['error'] = 'Este producto ya existe'
        context['listar_url'] = reverse_lazy('app:producto_lista')
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Producto actualizado exitosamente')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Ocurrió un error al actualizar el producto')
        return super().form_invalid(form)

@method_decorator(never_cache, name='dispatch')
class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'producto/eliminar.html'
    success_url = reverse_lazy('app:producto_lista')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'No autenticado'}, status=403)
        if not request.user.has_perm('app.delete_producto'):
            return JsonResponse({'error': 'No tienes permiso para eliminar este producto'}, status=403)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar producto'
        context['entidad'] = 'Eliminar producto'
        context['listar_url'] = reverse_lazy('app:producto_lista')
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Producto eliminado exitosamente')
        return super().delete(request, *args, **kwargs)
