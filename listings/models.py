import uuid
import datetime
from django.db import models
from django.utils import timezone
from products.models import Category, Product


class SaleListing(models.Model):
    listing_number = models.CharField(max_length=32, null=True, editable=False)
    is_listed = models.BooleanField(default=False)
    is_spotlight = models.BooleanField(default=False, blank=True)
    category = models.ForeignKey(Category, null=True,
                                 blank=True, on_delete=models.SET_NULL)
    company_name = models.CharField(max_length=256, null=True, blank=True)
    full_name = models.CharField(max_length=256, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=256, blank=False, null=False)
    call_between_hrs = models.CharField(max_length=256, blank=True, null=True)
    county = models.CharField(max_length=256, blank=False, null=False)
    area = models.CharField(max_length=256, blank=False, null=False)
    eircode = models.CharField(max_length=256, blank=True, null=True)
    property_type = models.CharField(max_length=256, blank=False, null=False)
    selling_type = models.CharField(max_length=256, blank=False, null=False)
    price = models.CharField(max_length=256, blank=False, null=False)
    no_of_bedrooms = models.IntegerField(blank=False, null=False)
    no_of_bathrooms = models.IntegerField(blank=False, null=False)
    facility_1 = models.CharField(max_length=256, blank=True, null=True)
    facility_2 = models.CharField(max_length=256, blank=True, null=True)
    facility_3 = models.CharField(max_length=256, blank=True, null=True)
    facility_4 = models.CharField(max_length=256, blank=True, null=True)
    facility_5 = models.CharField(max_length=256, blank=True, null=True)
    facility_6 = models.CharField(max_length=256, blank=True, null=True)
    floor_area = models.DecimalField(max_digits=10,
                                     decimal_places=2, null=False, blank=False)
    floor_area_type = models.CharField(max_length=256,
                                       blank=True, default='Square Meters')
    ber_rating = models.CharField(max_length=256, blank=False, null=False)
    tax_designation = models.CharField(max_length=256, blank=False, null=False)
    top_features_1 = models.CharField(max_length=100, blank=True, null=True)
    top_features_2 = models.CharField(max_length=100, blank=True, null=True)
    top_features_3 = models.CharField(max_length=100, blank=True, null=True)
    top_features_4 = models.CharField(max_length=100, blank=True, null=True)
    top_features_5 = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=False, null=False)
    images = models.ImageField()
    times_viewed = models.IntegerField(blank=True, null=True, editable=False)
    product = models.ForeignKey(Product, null=True,
                                blank=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(default=timezone.now)
    expiration_date = models.DateTimeField(null=True, blank=True)
    premium_expiration = models.DateTimeField(blank=True, null=True)

    def _generate_listing_number(self):

        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """ Override origonal save method
            to set the listing number if not already set """
        if self.product.is_premium:
            self.is_spotlight = True
        else:
            self.is_spotlight = False

        self.category = self.product.category

        if not self.listing_number:
            self.listing_number = self._generate_listing_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.listing_number


class RentListing(models.Model):
    listing_number = models.CharField(max_length=32, null=True, editable=False)
    is_listed = models.BooleanField(default=False)
    is_spotlight = models.BooleanField(default=False, blank=True)
    category = models.ForeignKey(Category, null=True,
                                 blank=True, on_delete=models.SET_NULL)
    company_name = models.CharField(max_length=256, null=True, blank=True)
    full_name = models.CharField(max_length=256, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=256, blank=False, null=False)
    call_between_hrs = models.CharField(max_length=256, blank=True, null=True)
    county = models.CharField(max_length=256, blank=False, null=False)
    area = models.CharField(max_length=256, blank=False, null=False)
    eircode = models.CharField(max_length=256, blank=True, null=True)
    property_type = models.CharField(max_length=256, blank=False, null=False)
    rent_type = models.CharField(max_length=256, blank=False, null=False)
    available_from = models.DateField(blank=False, null=False)
    lease_term = models.CharField(max_length=256, blank=False, null=False)
    price = models.CharField(max_length=256, blank=False, null=False)
    no_of_single_bedrooms = models.IntegerField(blank=False, null=False)
    no_of_double_bedrooms = models.IntegerField(blank=False, null=False)
    no_of_twin_bedrooms = models.IntegerField(blank=False, null=False)
    no_of_bathrooms = models.IntegerField(blank=False, null=False)
    furnishing = models.CharField(max_length=256, blank=False, null=False)
    facility_1 = models.CharField(max_length=256, blank=True, null=True)
    facility_2 = models.CharField(max_length=256, blank=True, null=True)
    facility_3 = models.CharField(max_length=256, blank=True, null=True)
    facility_4 = models.CharField(max_length=256, blank=True, null=True)
    facility_5 = models.CharField(max_length=256, blank=True, null=True)
    facility_6 = models.CharField(max_length=256, blank=True, null=True)
    floor_area = models.DecimalField(max_digits=10,
                                     decimal_places=2, null=False, blank=False)
    floor_area_type = models.CharField(max_length=256,
                                       blank=True, default='Square Meters')
    ber_rating = models.CharField(max_length=256, blank=False, null=False)
    description = models.TextField(max_length=1000, blank=False, null=False)
    images = models.ImageField()
    times_viewed = models.IntegerField(blank=True, null=True, editable=False)
    product = models.ForeignKey(Product, null=True,
                                blank=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(default=timezone.now)
    expiration_date = models.DateTimeField(null=True, blank=True)
    premium_expiration = models.DateTimeField(blank=True, null=True)

    def _generate_listing_number(self):

        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """ Override origonal save method
            to set the listing number if not already set """
        if self.product.is_premium:
            self.is_spotlight = True
        else:
            self.is_spotlight = False

        self.category = self.product.category

        if not self.listing_number:
            self.listing_number = self._generate_listing_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.listing_number
