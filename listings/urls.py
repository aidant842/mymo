from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_listings_view, name='listings'),
    path('sold/', views.sold_listings, name='sold_listings'),
    path('for_sale/', views.for_sale_listings, name='for_sale_listings'),
    path('for_sale/for-sale-by-owner/', views.for_sale_by_owner, name='for_sale_by_owner'),
    path('for_rent/', views.for_rent_listings, name='for_rent_listings'),
    path('for_sale/<int:listing_id>/', views.sale_listing_detail_view, name='sale_listing_detail'),
    path('for_rent/<int:listing_id>/', views.rent_listing_detail_view, name='rent_listing_detail'),
]
