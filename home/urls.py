from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('sitemap/', views.sitemap, name='sitemap'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('cookie-policy/', views.cookie_policy, name='cookie_policy'),
]
