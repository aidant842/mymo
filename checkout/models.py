import uuid

from django.db import models
from listings.models import SaleListing, RentListing
from products.models import Product
from profiles.models import UserProfile


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=32, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.IntegerField(null=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False,
                                  blank=False, default='')
    sale_listing = models.ForeignKey(SaleListing, on_delete=models.SET_NULL,
                                     null=True, editable=False)
    rent_listing = models.ForeignKey(RentListing, on_delete=models.SET_NULL,
                                     null=True, editable=False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,
                                null=True)

    def _generate_order_number(self):
        """ Generate a random, unique order number using UUID """

        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """ Override the origonal save method to set the order number
        if it hasn't already been set """

        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number
