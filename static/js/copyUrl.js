$('.clipboard').on('click', function() {
    var temp = $("<input>");
    var url = $(location).attr('href');
    $(".clipboard").append(temp);
    temp.val(url);
    temp.select();
    document.execCommand("copy");
    temp.remove();
    $("#copy-confirm").text("copied!");
});