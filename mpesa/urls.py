from django.urls import path
from . import views

urlpatterns = [
    path('', views.mpesapay, name='mpesapay'),
]
