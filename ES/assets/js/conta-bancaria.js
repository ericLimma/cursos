document.addEventListener('DOMContentLoaded', function () {
    let isChecked = true;
    let bankSection = document.getElementById('bank-section');
    let modalOverlay = document.getElementById('modal-overlay');
    let currentUser = null;
    let currentModal = null;

    class ContaBancaria {
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

    // Criação das instâncias das contas bancárias
    let contaJoao = new ContaBancaria('João Silva', '123456', 1000.00, 'Corrente');
    let contaMarilene = new ContaBancaria('Marilene Barbosa', '123456', 750.00, 'Corrente');
    let contaCleber = new ContaBancaria('Cleber Mendonça', '123456', 10000.00, 'Corrente');
    let contaRuth = new ContaBancaria('Ruth Ribeiro', '123456', 100.00, 'Corrente');

    document.getElementById('users-select').addEventListener('change', function (event) {
        if (currentUser) {
            currentUser.ocultarSaldo();
        }
        const selectedValue = event.target.value;

        switch (selectedValue) {
            case 'joao-silva':
                currentUser = contaJoao;
                break;
            case 'marilene-barbosa':
                currentUser = contaMarilene;
                break;
            case 'cleber-mendonca':
                currentUser = contaCleber;
                break;
            case 'ruth-ribeiro':
                currentUser = contaRuth;
                break;
            default:
                currentUser = null;
        }
    });

    document.getElementById('balance-checkbox').addEventListener('change', function () {
        if (!currentUser) {
            alert('Selecione um cliente');
            desmarcarCheckbox();
            return;
        }
        if (isChecked) {
            currentUser.exibirSaldo();
        } else {
            currentUser.ocultarSaldo();
        }
    });

    document.getElementById('btn-saque').addEventListener('click', function () {
        exibirModal('modal-saque');
    });

    document.getElementById('btn-deposito').addEventListener('click', function () {
        exibirModal('modal-deposito');
    });

    document.querySelectorAll('.close-modal').forEach(button => {
        button.addEventListener('click', function () {
            ocultarModal();
        });
    });

    modalOverlay.addEventListener('click', function (event) {
        if (event.target === modalOverlay) {
            ocultarModal();
        }
    });

    function exibirModal(idModal) {
        let modal = document.getElementById(idModal);
        modal.style.display = 'flex';
        modalOverlay.style.display = 'block';
        bankSection.style.filter = 'blur(5px)';
        currentModal = modal;
    }

    function ocultarModal() {
        if (currentModal) {
            currentModal.style.display = 'none';
            bankSection.style.filter = 'blur(0)';
            modalOverlay.style.display = 'none';
            currentModal = null;
        } else {
            console.warn('Nenhum modal está aberto para fechar.');
        }
    }
    function desmarcarCheckbox() {
        document.getElementById('balance-checkbox').checked = false;
    }
    contaRuth.depositarDinheiro(50);
    contaRuth.sacarDinheiro(10);
});
