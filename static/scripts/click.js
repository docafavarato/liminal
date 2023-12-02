function playSound(filename) {
    var audio = document.getElementById(filename);
    audio.play();
}

document.addEventListener('DOMContentLoaded', function () {
    var modal = document.getElementById('staticBackdrop');

    modal.addEventListener('click', function (event) {
        if (event.target === modal) {
            playSound("pop-up-blocked");
        }
    });
});