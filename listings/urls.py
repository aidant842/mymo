from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_listings_view, name='listings'),
    path('for_sale', views.for_sale_listings, name='for_sale_listings'),
    path('for_rent', views.for_rent_listings, name='for_rent_listings'),
]
