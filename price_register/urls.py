from django.urls import path
from . import views

urlpatterns = [
    path('', views.property_register, name='property_register'),
]
