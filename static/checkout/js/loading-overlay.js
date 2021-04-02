var form = document.querySelector('.checkout-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    $('#submitBtn').attr('disabled', true);
    $('.checkout-form').fadeToggle(100);
    $('.loader-bg').fadeToggle(100);
    form.submit();
});