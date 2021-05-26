from django.urls import path
from . import views

urlpatterns = [
    path('', views.property_register, name='property_register'),
    path('<int:listing_id>/', views.property_register_detail, name='property_register_detail'),
]
