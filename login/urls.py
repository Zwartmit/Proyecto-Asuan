from django.urls import path
from login.views import *
from .views import send_test_email

urlpatterns = [
    path('', loginFormView.as_view(), name='login'),
    path('logout', logoutRedirect.as_view(), name='logout'),
    path('send_email/', send_test_email, name='send_email')
]
