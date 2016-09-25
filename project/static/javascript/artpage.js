$(document).ready(function() {
    var back_button = $('.carousel-button-back > .carousel-button').first();
    var forward_button = $('.carousel-button-forward > .carousel-button').first();
    $(document).keydown(function(e) {
        switch (e.keyCode) {
            case 37:
                if (back_button) {
                    window.location.href = back_button.attr('href');
                }
                break;
            case 39:
                if (forward_button) {
                    window.location.href = forward_button.attr('href');
                }
                break;
        }
    });
});
