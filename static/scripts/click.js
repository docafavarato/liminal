document.getElementById('click').addEventListener('canplaythrough', function() {
    document.getElementById('trash').addEventListener('click', function() {
        var audio = document.getElementById('click');
        audio.play();
        mostrarErro();
    });
});