from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('public_profile/<int:profile_id>/', views.public_profile, name='public_profile'),
    path('remove_listing/<int:product_id>/', views.delete_listing, name='delete_listing'),
]
