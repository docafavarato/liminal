
document.addEventListener('DOMContentLoaded', function () {
    var modals = document.querySelectorAll(".modal");
    
    modals.forEach(modal => {
        $(modal).on("shown.bs.modal", function () {
            var mouseX = event.clientX;
            var mouseY = event.clientY;

            var rand = randomIntFromInterval(1, 2);
            switch (rand) {
                case 1:
                    modal.style.left = (mouseX - 20) + "px";
                    modal.style.top = (mouseY - 20) + "px";
                    break;
                case 2:
                    modal.style.left = (mouseX + 200) + "px";
                    modal.style.top = (mouseY - 20) + "px";
            }
        });
    });
});

function randomIntFromInterval(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
}

document.addEventListener("DOMContentLoaded", function() {
    var modals = document.getElementsByClassName("modal");

    for (var i = 0; i < modals.length; i++) {
        ["click", "mousedown"].forEach(ev => {
            modals[i].addEventListener(ev, function() {
                var maiorZIndex = 0;
                var modals = document.getElementsByClassName("modal");
    
                for (var j = 0; j < modals.length; j++) {
                    var zIndex = parseInt(window.getComputedStyle(modals[j]).getPropertyValue('z-index'));
                    if (!isNaN(zIndex) && zIndex > maiorZIndex) {
                        maiorZIndex = zIndex;
                    }
                }
    
                this.style.zIndex = maiorZIndex + 1;
            });
        });
    }
});

function playSound(filename) {
    var audio = document.getElementById(filename);
    audio.play();

    ignore = ["click", "error", "pop-up-blocked", "exclamation", "error-sound"]

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

function autoResize() {
    var textareas = document.querySelectorAll('textarea');
    textareas.forEach(textarea => {
        textarea.style.height = "";
        textarea.style.height = textarea.scrollHeight + "px";
    });
}

$("textarea").each(function () {
    this.setAttribute("style", "height:" + (this.scrollHeight) + "px;overflow-y:hidden;");
});
