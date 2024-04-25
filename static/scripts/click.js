function playSound(filename) {
    var audio = document.getElementById(filename);
    audio.play();

    ignore = ["click", "error", "pop-up-blocked"]

    if (!ignore.includes(filename)) {
        document.querySelector("#toast .toast-body").textContent = "Now playing: " + filename;

        const toast = bootstrap.Toast.getOrCreateInstance(document.getElementById('toast'));
        toast.show();
    }
}

document.addEventListener('DOMContentLoaded', function () {
    var modals = document.querySelectorAll('.modal');

    modals.forEach(function (modal) {
        modal.addEventListener('click', function (event) {
            if (event.target === modal) {
                playSound("pop-up-blocked");
            }
        });
    });
});
