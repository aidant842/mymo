const addIcons = () => {
    let anchor = document.querySelectorAll('.socialaccount_provider');
    anchor[0].innerHTML = '<span class="mx-1"><i class="fab fa-facebook-f"></i></span><span>Use Facebook</span>';
    anchor[1].innerHTML = '<span class="mx-1"><i class="fab fa-google"></i></span><span>Use Google</span>';
    /* anchor[1].innerHTML = '<i class="fab fa-twitter"></i> Twitter'; */
};


addIcons();