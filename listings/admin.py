from django.contrib import admin
from .models import SaleListing, RentListing


class SaleListingAdmin(admin.ModelAdmin):
    list_display = (
        'listing_number',
        'company_name',
        'full_name',
        'category',
        'price',
        'is_listed',
        'is_spotlight',
        'product',
        'expiration_date'
    )


class RentListingAdmin(admin.ModelAdmin):
    list_display = (
        'listing_number',
        'company_name',
        'full_name',
        'category',
        'price',
        'is_listed',
        'is_spotlight',
        'product',
        'expiration_date'
    )


admin.site.register(SaleListing, SaleListingAdmin)
admin.site.register(RentListing, RentListingAdmin)
