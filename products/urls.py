from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_view, name='products')
]
