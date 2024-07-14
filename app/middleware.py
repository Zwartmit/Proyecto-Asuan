from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.urls import resolve, reverse

class NoCacheMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response['Pragma'] = 'no-cache'
        response['Expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
        return response

class LoginRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        public_paths = [
            reverse('index'),
            reverse('login'),
            reverse('logout'),
        ]
        if not request.user.is_authenticated and request.path not in public_paths:
            return redirect('login')
