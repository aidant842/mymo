const addIcons = () => {
    let anchor = document.querySelectorAll('.socialaccount_provider');
    anchor[0].innerHTML = '<i class="fab fa-google"></i> Google';
    anchor[1].innerHTML = '<i class="fab fa-facebook-f"></i> Facebook';
    /* anchor[1].innerHTML = '<i class="fab fa-twitter"></i> Twitter'; */
};


addIcons();