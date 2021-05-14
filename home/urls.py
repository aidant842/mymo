from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('sitemap/', views.sitemap, name='sitemap'),
    path('cookie-declaration/', views.cookie_declaration, name='cookie_declaration'),
]
