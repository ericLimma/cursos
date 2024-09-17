//set listeners
import { showAlert } from "./showAlert.js";
import { cadastrarDespesa } from "./cadastrarDespesa.js";
import { pesquisarDespesa } from "./pesquisarDespesa.js";
import { carregarListaDespesas } from "./carregarListaDespesas.js";
import { limparCampos } from "./limparCampos.js";
import { modal } from "./modal.js";

export function setListeners() {
        setButtonListener('search-button', pesquisarDespesa);
        setButtonListener('erase-search-button', () => {
                limparCampos();
                carregarListaDespesas();
        });

        setDayListener('day');
        setValorListener('valor');
        carregarListaDespesas();

        setButtonListener('add-expense', () => {
                modal.abrirModal();  // Usa a instância global do modal
        });

        setButtonListener('button-clear-storage', () => {
                showAlert('error', 'Local Storage Limpo');
                localStorage.clear();
                location.reload();
        });
}

export function setModalListeners(id) {

        const saveButton = document.getElementById('save-expense');
        const newListener = () => cadastrarDespesa(id);

        saveButton.removeEventListener('click', saveButton._listener);
        saveButton.addEventListener('click', newListener);

        saveButton._listener = newListener;

        setDayListener('new-expense-day');
        setValorListener('new-expense-value');
}

// Função para adicionar listeners a botões
export function setButtonListener(buttonId, callback) {
        const button = document.getElementById(buttonId);
        if (button) {
                button.addEventListener('click', callback);
        } else {
                console.log(`Button with ID ${buttonId} does not exist.`);
        }
}

// Função para adicionar listeners a botões
function setDayListener(id) {

        const day = document.getElementById(id);

        day.addEventListener('change', () => {
                const dayValue = parseInt(day.value, 10);
                const monthValue = document.getElementById('month').value;

                if (dayValue > 31 || (monthValue === '2' && dayValue > 28)) {
                        day.classList.add('ipt-erro');
                        day.value = '';
                        showAlert('error', 'Dia Inválido para esse mês');
                } else {
                        day.classList.remove('ipt-erro');
                }
        });

        day.addEventListener('input', () => {
                day.value = day.value.replace(/\D/g, '').slice(0, 2);
        });

        day.addEventListener('keydown', e => {
                if (e.key === 'Enter') pesquisarDespesa()
        })
}

// Listener para o campo 'valor'
function setValorListener(id) {

        const valor = document.getElementById(id);

        valor.addEventListener('input', () => {

                valor.value = formatCurrency(valor.value);
                valor.setSelectionRange(valor.value.length, valor.value.length);
        });

        valor.addEventListener('focus', () => {
                valor.setSelectionRange(valor.value.length, valor.value.length);
        });

        valor.addEventListener('keydown', e => {
                if (e.key === 'Enter') {
                        id === 'new-expense-value' ? cadastrarDespesa() : pesquisarDespesa();
                }
        })
}

function formatCurrency(value) {
        const cleanedValue = value.replace(/[^\d]/g, ''); // Remove caracteres não numéricos
        const numericValue = parseInt(cleanedValue, 10) || 0; // Converte para número
        return (numericValue / 100).toFixed(2).replace('.', ','); // Formatação BR (0,00)
}