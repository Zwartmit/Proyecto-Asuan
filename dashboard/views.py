from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.deprecation import MiddlewareMixin

class dashView(TemplateView):
    
    template_name = 'dashboard.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Administración'
        return context
    @login_required
    def dashboard_view(request):
        return render(request, 'dashboard.html')
