const bttLink = () => {
    //Get the button:
    mybutton = document.querySelector(".bttLink");

    // When the user scrolls down 20px from the top of the document, show the button
    window.onscroll = function() {scrollFunction()};

    function scrollFunction() {
        if (document.body.scrollTop > 400 || document.documentElement.scrollTop > 400) {
            mybutton.classList.add('bttLinkTranslate');
        } else if (document.body.scrollTop < 300 || document.documentElement.scrollTop < 300){
            mybutton.classList.remove('bttLinkTranslate');
        }
    }

    mybutton.onclick = function() {
        topFunction();
    }

    // When the user clicks on the button, scroll to the top of the document
    function topFunction() {
        document.body.scrollTop = 0; // For Safari
        document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
    } 
}

document.body.onload = function () {
  document.querySelector("#loader-bg").classList.add("hidden");
};

bttLink();