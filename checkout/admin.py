from django.contrib import admin
from .models import Order
from listings.models import SaleListing, RentListing


class SaleListingOrderAdmin(admin.StackedInline):
    model = SaleListing


class RentListingOrderAdmin(admin.StackedInline):
    model = RentListing


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_number',
        'date',
        'email',
        'product',
        'order_total',
        'date',
    )

    readonly_fields = (
        'order_number',
        'sale_listing',
        'rent_listing',
        'date',
        'stripe_pid',
        'order_total',
        'product',
    )

    fields = (
        'order_number',
        'full_name',
        'email',
        'phone_number',
        'order_total',
        'stripe_pid',
        'product',
        'sale_listing',
        'rent_listing',
        'date',
    )


admin.site.register(Order, OrderAdmin)
