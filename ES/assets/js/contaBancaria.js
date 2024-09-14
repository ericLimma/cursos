export class ContaBancaria {
    constructor(nomeTitular, numConta, saldoConta, tipoConta) {
        this.nomeTitular = nomeTitular;
        this.numConta = numConta;
        this.saldoConta = saldoConta;
        this.tipoConta = tipoConta;
    }

    exibirSaldo() {
        let userName = document.getElementById('user-name');
        let balance = document.getElementById('balance-display');

        userName.textContent = this.nomeTitular;
        balance.textContent = `R$ ${this.saldoConta}`;
        isChecked = false;
    }

    ocultarSaldo() {
        let userName = document.getElementById('user-name');
        let balance = document.getElementById('balance-display');

        // Cria o elemento de placeholder
        let placeholderSpan = document.createElement('span');
        placeholderSpan.className = 'placeholder-span';

        // Substitui o conteúdo atual pelos placeholders
        userName.innerHTML = '';
        balance.innerHTML = '';
        userName.appendChild(placeholderSpan.cloneNode(true));
        balance.appendChild(placeholderSpan.cloneNode(true));

        isChecked = true;
        desmarcarCheckbox();
    }

    sacarDinheiro(valorSaque) {
        this.saldoConta -= valorSaque;
    }

    depositarDinheiro(valorDeposito) {
        this.saldoConta += valorDeposito;
    }

}
