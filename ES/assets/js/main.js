// main.js
import { ContaBancaria } from "./contaBancaria.js";
import { initializeApp } from "./envetHandler.js";


// Criação das instâncias das contas bancárias
let contaJoao = new ContaBancaria('João Silva', '123456', 1000.00, 'Corrente');
let contaMarilene = new ContaBancaria('Marilene Barbosa', '123456', 750.00, 'Corrente');
let contaCleber = new ContaBancaria('Cleber Mendonça', '123456', 10000.00, 'Corrente');
let contaRuth = new ContaBancaria('Ruth Ribeiro', '123456', 100.00, 'Corrente');

document.addEventListener('DOMContentLoaded', function () {
    // Passa as instâncias das contas para initializeApp
       initializeApp(contaJoao, contaMarilene, contaCleber, contaRuth);
    
        // Exemplos de uso das contas
        contaRuth.depositarDinheiro(50);
        contaRuth.sacarDinheiro(10);
});
