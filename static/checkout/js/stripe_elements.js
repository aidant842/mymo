var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var card = elements.create('card')
card.mount('#card-element');

// Handle realtime validation errors on the card element

card.addEventListener('change', function(event){
    var errorDiv = document.querySelector('.card-errors');
    if (event.error) {
        var html =
            `<span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>`;
            $(errorDiv).html(html);
    }
    else {
        errorDiv.textContent = '';
    }
});

// Handle form submit

var form = document.querySelector('.checkout-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submitBtn').attr('disabled', true);
    $('.checkout-form').fadeToggle(100);
    $('.loader-bg').fadeToggle(100);
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret
    }
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function() {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value)
                }
            }
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.querySelector('.card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                $('.checkout-form').fadeToggle(100);
                $('.loader-bg').fadeToggle(100);
                card.update({ 'disabled': false});
                $('#submitBtn').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    /* form.submit(); */
                }
            }
        });
    }).fail(function() {
        // Reload to show user the fail message
        location.reload();
    });
});
