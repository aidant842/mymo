from django.contrib import admin
from .models import SaleListing, RentListing, SaleListingImage, RentListingImage


class SaleListingImageAdmin(admin.StackedInline):
    model = SaleListingImage


class RentListingImageAdmin(admin.StackedInline):
    model = RentListingImage


class SaleListingAdmin(admin.ModelAdmin):
    inlines = [SaleListingImageAdmin]
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

    readonly_fields = (
        'category',
        'product',
        'date_created',
    )


class RentListingAdmin(admin.ModelAdmin):
    inlines = [RentListingImageAdmin]
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


@admin.register(SaleListingImage)
class SaleListingImageAdmin(admin.ModelAdmin):
    pass


@admin.register(RentListingImage)
class RentListingImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(SaleListing, SaleListingAdmin)
admin.site.register(RentListing, RentListingAdmin)
