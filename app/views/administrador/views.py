import django
import os
import re
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.db.models import ProtectedError
from app.models import Administrador
from app.forms import AdministradorForm

@method_decorator(login_required, name='dispatch')
class AdministradorListView(ListView):
    model = Administrador
    template_name = 'administrador/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de administradores'
        context['entidad'] = 'Listado de administradores'
        context['listar_url'] = reverse_lazy('app:administrador_lista')
        context['crear_url'] = reverse_lazy('app:administrador_crear')
        context['has_permission'] = self.request.user.has_perm('app.view_administrador')

        if self.request.user.groups.filter(name='Operador').exists():
            context['can_add'] = False
        else:
            context['can_add'] = self.request.user.has_perm('app.add_administrador')

        return context

@method_decorator(login_required, name='dispatch')
class AdministradorCreateView(CreateView):
    model = Administrador
    form_class = AdministradorForm
    template_name = 'administrador/crear.html'
    success_url = reverse_lazy('app:administrador_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registrar administrador'
        context['entidad'] = 'Registrar administrador'
        context['listar_url'] = reverse_lazy('app:administrador_lista')
        context['has_permission'] = not self.request.user.groups.filter(name='Operador').exists() and self.request.user.has_perm('app.add_administrador')
        return context

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.has_perm('app.add_administrador') or self.request.user.groups.filter(name='Operador').exists():
            list_context = AdministradorListView.as_view()(request, *args, **kwargs).context_data
            return render(request, 'administrador/listar.html', list_context)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        nombre = form.cleaned_data.get('nombre').lower()
        numero_documento = form.cleaned_data.get('numero_documento')
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password1 = form.cleaned_data.get("password")
        password2 = form.cleaned_data.get("conf_password")

        if Administrador.objects.filter(numero_documento=numero_documento).exists():
            form.add_error('numero_documento', 'Ya existe un administrador registrado con ese número de documento.')
            return self.form_invalid(form)

        # Validaciones de nombre de usuario y correo electrónico
        if User.objects.filter(username=username).exists():
            form.add_error('username', 'Este nombre de usuario ya está en uso.')
            return self.form_invalid(form)
        
        if User.objects.filter(email=email).exists():
            form.add_error('email', 'Este correo electrónico ya está en uso.')
            return self.form_invalid(form)
        
        # Validación de contraseñas
        if password1 or password2:
            if not password1 or not password2:
                form.add_error('password', 'Ambos campos de contraseña deben ser completados si se proporciona una contraseña.')
                return self.form_invalid(form)
            
            if password1 != password2:
                form.add_error('conf_password', 'Las contraseñas no coinciden.')
                return self.form_invalid(form)
            
            if len(password1) < 8:
                form.add_error('password', 'La contraseña debe tener al menos 8 caracteres.')
                return self.form_invalid(form)
            
            if not re.search(r'[A-Z]', password1):
                form.add_error('password', 'La contraseña debe incluir al menos una letra mayúscula.')
                return self.form_invalid(form)
            
            if not re.search(r'[0-9]', password1):
                form.add_error('password', 'La contraseña debe incluir al menos un número.')
                return self.form_invalid(form)
            
            # Si las contraseñas son válidas, haz el hash de la contraseña y guárdalo
            form.instance.user.password = make_password(password1)

        # Llama al método `form_valid` original para continuar con el procesamiento del formulario
        response = super().form_valid(form)
        success_url = f"{self.get_success_url()}?created=true"
        return redirect(success_url)

@method_decorator(login_required, name='dispatch')
class AdministradorUpdateView(UpdateView):
    model = Administrador
    form_class = AdministradorForm
    template_name = 'administrador/crear.html'
    success_url = reverse_lazy('app:administrador_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar administrador'
        context['entidad'] = 'Editar administrador'
        context['listar_url'] = reverse_lazy('app:administrador_lista')
        context['has_permission'] = not self.request.user.groups.filter(name='Operador').exists() and self.request.user.has_perm('app.change_administrador')
        return context

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.has_perm('app.change_administrador') or self.request.user.groups.filter(name='Operador').exists():
            list_context = AdministradorListView.as_view()(request, *args, **kwargs).context_data
            return render(request, 'administrador/listar.html', list_context)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        password1 = form.cleaned_data.get("password")
        password2 = form.cleaned_data.get("conf_password")

        # Validación de contraseñas
        if password1 or password2:
            if not password1 or not password2:
                form.add_error('password', 'Ambos campos de contraseña deben ser completados si se proporciona una contraseña.')
                return self.form_invalid(form)
            
            if password1 != password2:
                form.add_error('conf_password', 'Las contraseñas no coinciden.')
                return self.form_invalid(form)
            
            if len(password1) < 8:
                form.add_error('password', 'La contraseña debe tener al menos 8 caracteres.')
                return self.form_invalid(form)
            
            if not re.search(r'[A-Z]', password1):
                form.add_error('password', 'La contraseña debe incluir al menos una letra mayúscula.')
                return self.form_invalid(form)
            
            if not re.search(r'[0-9]', password1):
                form.add_error('password', 'La contraseña debe incluir al menos un número.')
                return self.form_invalid(form)
            
            # Si las contraseñas son válidas, haz el hash de la contraseña y guárdalo
            self.object.user.password = make_password(password1)

        # Llama al método `form_valid` original para continuar con el procesamiento del formulario
        response = super().form_valid(form)
        success_url = f"{self.get_success_url()}?updated=True"
        return redirect(success_url)

@method_decorator(login_required, name='dispatch')
class AdministradorDeleteView(DeleteView):
    model = Administrador
    template_name = 'administrador/eliminar.html'
    success_url = reverse_lazy('app:administrador_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar administrador'
        context['entidad'] = 'Eliminar administrador'
        context['listar_url'] = reverse_lazy('app:administrador_lista')
        context['has_permission'] = not self.request.user.groups.filter(name='Operador').exists() and self.request.user.has_perm('app.delete_administrador')
        return context

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.has_perm('app.delete_administrador') or self.request.user.groups.filter(name='Operador').exists():
            list_context = AdministradorListView.as_view()(request, *args, **kwargs).context_data
            return render(request, 'administrador/listar.html', list_context)
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
            return JsonResponse({'success': True, 'message': 'Administrador eliminado con éxito.'})
        except ProtectedError:
            return JsonResponse({'success': False, 'message': 'No se puede eliminar el administrador.'})