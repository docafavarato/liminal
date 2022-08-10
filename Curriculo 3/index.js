function lua() {
    document.body.style.backgroundColor = '#2b2a2a';
    document.getElementById('github').style.color = 'white';
    document.getElementById('linkedin').style.color = 'white';
    document.getElementById('lua').style.color = 'white';
    document.getElementById('sol').style.color = 'white';
    document.getElementById('obj').style.color = 'rgb(245, 234, 219)';
    document.getElementById('objT').style.color = 'white';
    document.getElementById('exp').style.color = 'white';
    document.getElementById('objt').style.color = 'white';
    document.getElementById('nome').style.color = 'rgb(245, 234, 219)';
    document.getElementById('exp').style.color = 'white';
    document.getElementById('target').style.color = 'white';
    document.getElementById('ob').style.color = 'white';
}

function sol(){
    document.body.style.backgroundColor = '#d6d6d6';
    document.getElementById('github').style.color = 'black';
    document.getElementById('linkedin').style.color = 'black';
    document.getElementById('lua').style.color = 'black';
    document.getElementById('sol').style.color = 'black';
    document.getElementById('obj').style.color = 'black';
    document.getElementById('objT').style.color = 'black';
    document.getElementById('nome').style.color = 'black';
    document.getElementById('objt').style.color = 'black';
    document.getElementById('ob').style.color = 'black';
    document.getElementById('exp').style.color = 'black';
    document.getElementById('target').style.color = 'black';
}

function enviar(){
    nome = document.getElementById('nomeIn').value;
    email = document.getElementById('emailIn').value;
    texto = document.getElementById('textIn').value;

    window.open(`mailto:docafavarato@gmail.com?subject=${nome}&body=${texto}`);
}   