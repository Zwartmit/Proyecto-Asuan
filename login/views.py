from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.core.mail import send_mail

class loginFormView(LoginView):
    template_name = "login.html"
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Iniciar sesión'
        return context

class logoutRedirect(RedirectView):
    pattern_name = 'login'
    
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)

def send_test_email(request):
    if request.method == 'POST':
        send_mail(
            'Asunto del correo',
            'Aquí está el mensaje.',
            'davidcubides05@gmail.com',  # Cambia esto por tu dirección de correo de Gmail
            ['davidcubides05@gmail.com'],  # Cambia esto por la dirección de correo del destinatario
            fail_silently=False,
        )
        return HttpResponse("Correo enviado")
    return render(request, 'send_email.html')