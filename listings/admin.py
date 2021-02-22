from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = (
        'listing_number',
        'company_name',
        'full_name',
        'category',
        'price',
        'is_listed',
        'is_spotlight',
        'product',
    )


admin.site.register(Listing, ListingAdmin)
