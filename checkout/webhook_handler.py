from django.http import HttpResponse
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import OrderForm
from .models import Order
from listings.models import SaleListing, RentListing
from products.models import Product
from profiles.models import UserProfile

import time
import datetime


class StripeWH_Handler():
    """ Handle stripe webhooks """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """ Send the user a confirmation email """

        cust_email = order.email
        subject = render_to_string('checkout/confirmation_emails/confirmation_email_subject.txt', {'order':order})

        body = render_to_string('checkout/confirmation_emails/confirmation_email_body.txt',
        {'order': order, 'contact_email': settings.REPLY_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """ Handle a generic/unknown webhook event """

        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """ Handle the payment_intent.succeeded webhook """

        intent = event.data.object
        pid = intent.id
        product_id = intent.metadata.product_id
        listing_id = intent.metadata.listing_id
        product = Product.objects.get(pk=product_id)
        username = intent.metadata.username
        profile = UserProfile.objects.get(user__username=username)
        billing_details = intent.charges.data[0].billing_details

        if product.category.name == 'sale':
            listing = SaleListing.objects.get(pk=listing_id)
            order_exists = False
            attempt = 1
            while attempt <= 5:
                try:
                    order = Order.objects.get(
                        stripe_pid=pid,
                    )
                    order_exists = True
                    break
                except Order.DoesNotExist:
                    attempt += 1
                    time.sleep(1)
            if order_exists:
                self._send_confirmation_email(order)
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already exists in database',
                    status=200)
            else:
                order = None
                try:
                    listing.is_paid = True
                    listing.user_profile = profile
                    listing.expiration_date = (timezone.now()
                                               + datetime.timedelta(days=365))
                    listing.save()
                    order = Order.objects.create(
                        user_profile=profile,
                        full_name=billing_details.name,
                        email=billing_details.email,
                        phone_number=billing_details.phone,
                        order_total=listing.product.price,
                        stripe_pid=pid,
                        sale_listing=listing,
                        product=product,
                    )
                except Exception as e:
                    if order:
                        order.delete()
                    return HttpResponse(
                        content=f'Webhook received: {event["type"]} | ERROR: {e}',
                        status=500
                        )
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook recieved. {event["type"]}'
                ' | SUCCESS: Created order in webhook',
                status=200
            )

        # IF RENT
        elif product.category.name == 'rent':
            listing = RentListing.objects.get(pk=listing_id)
            order_exists = False
            attempt = 1
            while attempt <= 5:
                try:
                    order = Order.objects.get(
                        stripe_pid=pid,
                    )
                    order_exists = True
                    break
                except Order.DoesNotExist:
                    attempt += 1
                    time.sleep(1)
            if order_exists:
                # Send Confirmation Email ------------
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already exists in database',
                    status=200)
            else:
                order = None
                try:
                    listing.is_paid = True
                    listing.user_profile = profile
                    listing.expiration_date = (timezone.now()
                                               + datetime.timedelta(days=90))
                    listing.save()
                    order = Order.objects.create(
                        user_profile=profile,
                        full_name=billing_details.name,
                        email=billing_details.email,
                        phone_number=billing_details.phone,
                        order_total=listing.product.price,
                        stripe_pid=pid,
                        rent_listing=listing,
                        product=product,
                    )
                except Exception as e:
                    if order:
                        order.delete()
                    return HttpResponse(
                        content=f'Webhook received: {event["type"]} | ERROR: {e}',
                        status=500)
            # self._send_confirmation_email(order) SEND EMAIL
            return HttpResponse(
            content=f'Webhook recieved. {event["type"]}'
            ' | SUCCESS: Created order in webhook',
            status=200
            )

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """ Handle the payment_intent.payment_failed intent succeeded webhook """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )