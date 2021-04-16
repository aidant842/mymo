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
        'is_paid',
        'is_spotlight',
        'product',
        'expiration_date'
    )

    readonly_fields = (
        'category',
        'date_created',
        'times_viewed',
    )

    search_fields = ['listing_number']

    def save_model(self, request, obj, form, change):
        obj.save()

        for afile in request.FILES.getlist('photos_multiple'):
            obj.listingImages.create(images=afile)


class RentListingAdmin(admin.ModelAdmin):
    inlines = [RentListingImageAdmin]
    list_display = (
        'listing_number',
        'company_name',
        'full_name',
        'category',
        'price',
        'is_listed',
        'is_paid',
        'is_spotlight',
        'product',
        'expiration_date'
    )

    readonly_fields = (
        'category',
        'date_created',
        'times_viewed',
    )

    search_fields = ['listing_number']

    def save_model(self, request, obj, form, change):
        obj.save()

        for afile in request.FILES.getlist('photos_multiple'):
            obj.listingImages.create(images=afile)


@admin.register(SaleListingImage)
class SaleListingImageAdmin(admin.ModelAdmin):
    pass


@admin.register(RentListingImage)
class RentListingImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(SaleListing, SaleListingAdmin)
admin.site.register(RentListing, RentListingAdmin)
