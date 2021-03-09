from django.http import HttpResponse


class StripeWH_Hanlder:
    """ Handle stripe webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle a generic/unknown webhook event """

        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """ Handle the payment_intent.succeeded webhook """

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