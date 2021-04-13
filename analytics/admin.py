from django.contrib import admin
from .models import ListingAnalytics


class ListingAnalyticsAdmin(admin.ModelAdmin):
    list_display = (
        'average_listing_views',
    )

    readonly_fields = (
        'id',
        'average_listing_views',
    )


admin.site.register(ListingAnalytics, ListingAnalyticsAdmin)


