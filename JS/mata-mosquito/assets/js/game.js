
let altura = 0;
let largura = 0;
let vidas = 1;
let tempo = 15;
let tempoCriarMosca = 1500;
let nivel = window.location.search.replace('?', '');


if (nivel === 'normal') {
    tempoCriarMosca = 1500;

} else if (nivel === 'dificil') {
    tempoCriarMosca = 1000;

} else if (nivel === 'exterminador') {
    tempoCriarMosca = 750;

};


document.getElementById('cronometro').innerHTML = tempo;

function ajustaTamanhoPalco() {
    altura = window.innerHeight;
    largura = window.innerWidth;

    console.log(altura, largura);
};

ajustaTamanhoPalco();

let criarMosca = setInterval(function () {
    posicaoRandomica();
}, tempoCriarMosca);

let cronometro = setInterval(function () {
    tempo -= 1;
    if (tempo < 0) {
        clearInterval(cronometro);
        clearInterval(criarMosca);
        window.location.href = 'you-won.html';
    } else {
        document.getElementById('cronometro').innerHTML = tempo;
    };
}, 1000);

function posicaoRandomica() {

    if (document.getElementById('mosca')) {
        document.getElementById('mosca').remove();

        if (vidas > 3) {
            window.location.href = 'game-over.html'
        } else {
            document.getElementById(`v-${vidas}`).src = 'assets/img/coracao_vazio.png';
            vidas++;
        }
    }

    let posicaoY = Math.floor(Math.random() * altura) - 90; //cria uma posição aleatória, sutraindo 90px, para que o objeto nao saia de tela
    let posicaoX = Math.floor(Math.random() * largura) - 90;

    posicaoY = posicaoY < 0 ? 0 : posicaoY; //impeade que a posição seja menor que 0
    posicaoX = posicaoX < 0 ? 0 : posicaoX; //impeade que a posição seja menor que 0

    //mosca
    let mosca = document.createElement('img'); //cria o objeto da mosca dentro do html.
    mosca.src = 'assets/img/mosca.png';
    mosca.className = `${tamanhoAleatorio()}  ${ladoAleatorio()}`;
    mosca.style.top = `${posicaoY}px`;
    mosca.style.left = `${posicaoX}px`;
    mosca.id = 'mosca';
    mosca.onclick = function () {
        this.remove();
    };
    document.body.appendChild(mosca);


};
function tamanhoAleatorio() {
    let classe = Math.floor(Math.random() * 3);

    switch (classe) {
        case 0:
            return 'mosca-1';
        case 1:
            return 'mosca-2';
        case 2:
            return 'mosca-3';

    };
};
function ladoAleatorio() {
    let classe = Math.floor(Math.random() * 2);

    switch (classe) {
        case 0:
            return 'lado-a';
        case 1:
            return 'lado-b';

    };
};