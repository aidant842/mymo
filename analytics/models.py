from django.db import models


class ListingAnalytics(models.Model):
    average_listing_views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.average_listing_views)
