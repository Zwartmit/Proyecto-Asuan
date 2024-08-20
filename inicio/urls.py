from django.urls import path
from inicio.views import *

urlpatterns = [
    path('', indexView.as_view(), name='index'),
    path('contact/', contact, name='contact')
]
