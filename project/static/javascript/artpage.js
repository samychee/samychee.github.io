document.addEventListener("DOMContentLoaded", function() {
    var videos = document.getElementsByClassName('artpage-video');
    for (var i = 0; i < videos.length; i++) {
        var video = videos[i];
        video.onclick = function() {
            if (video.paused) {
                video.play();
            } else {
                video.pause();
            }
        }
    }

    var back_button = document.getElementsByClassName('carousel-button-back');
    var forward_button = document.getElementsByClassName('carousel-button-forward');
    if (back_button.length) {
        back_button = back_button[0];
    } else {
        back_button = null;
    }
    if (forward_button.length) {
        forward_button = forward_button[0];
    } else {
        forward_button = null;
    }
    if (back_button || forward_button) {
        document.onkeydown = function(e) {
            e = e || window.event;
            switch (e.keyCode) {
                case 37:
                    if (back_button) {
                        window.location.href = back_button.href;
                    }
                    break;
                case 39:
                    if (forward_button) {
                        window.location.href = forward_button.href;
                    }
                    break;
            }
        }
    }
});
