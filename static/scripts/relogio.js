function atualizarRelogio() {
    var agora = new Date();
    var horas = agora.getHours();
    var minutos = agora.getMinutes();
    var periodo = horas >= 12 ? 'PM' : 'AM';

    horas = horas % 12 || 12;

    horas = horas < 10 ? '0' + horas : horas;
    minutos = minutos < 10 ? '0' + minutos : minutos;

    var relogioElement = document.getElementById('relogio');
    relogioElement.innerHTML = horas + ':' + minutos + ' ' + periodo;

    setTimeout(atualizarRelogio, 60000);
}

window.onload = function() {
    atualizarRelogio();
};

