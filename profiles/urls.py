from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('remove_listing/<int:listing_id>/', views.delete_listing, name='delete_listing'),
]
