from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('remove_listing/<int:listing_id>/', views.delete_listing, name='delete_listing'),
    path('favourite_sale_add/<int:listing_id>/', views.favourite_sale_add, name='favourite_sale_add'),
    path('favourite_rent_add/<int:listing_id>/', views.favourite_rent_add, name='favourite_rent_add'),
]

""" path('save_sale_listing/<int:listing_id>/', views.save_sale_listing, name='save_sale_listing'),
path('save_rent_listing/<int:listing_id>/', views.save_rent_listing, name='save_rent_listing'), """
