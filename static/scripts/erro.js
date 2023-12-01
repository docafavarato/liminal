function mostrarErro() {
  var audio = document.getElementById('click');
  audio.play();

  var overlay = document.getElementById('erroOverlay');
  overlay.style.display = 'block';
}

function fecharErro() {
  var audio = document.getElementById('click');
  audio.play();
  
  var overlay = document.getElementById('erroOverlay');
  overlay.style.display = 'none';
}