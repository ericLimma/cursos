// eventHandler.js
function initializeApp(contaJoao, contaMarilene, contaCleber, contaRuth) {
    let isChecked = true;
    let bankSection = document.getElementById('bank-section');
    let modalOverlay = document.getElementById('modal-overlay');
    let currentUser = null;
    let currentModal = null;

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
}
export { initializeApp };