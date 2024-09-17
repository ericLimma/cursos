import { limparCampos } from "./limparCampos.js";
import { setModalListeners } from "./setListeners.js";

export function openModal() {
        return new Promise((resolve) => {
                const modalOverlay = document.getElementById('modal-overlay');
                const modalConfirm = document.getElementById('modal-confirm');
                const modalCancel = document.getElementById('modal-cancel');

                function handleConfirm() {
                        closeModal();
                        resolve(true);  // Retorna true quando confirmado
                }

                function handleCancel() {
                        closeModal();
                        resolve(false);  // Retorna false quando cancelado
                }

                function closeModal() {
                        modalOverlay.classList.remove('show');
                        // Remove os event listeners ao fechar
                        document.removeEventListener('keydown', handleKeyDown);
                        modalConfirm.removeEventListener('click', handleConfirm);
                        modalCancel.removeEventListener('click', handleCancel);
                }

                function handleKeyDown(event) {
                        if (event.key === 'Enter') {
                                handleConfirm();
                        }
                }

                // Adiciona os event listeners
                document.addEventListener('keydown', handleKeyDown);
                modalConfirm.addEventListener('click', handleConfirm);
                modalCancel.addEventListener('click', handleCancel);

                modalOverlay.classList.add('show');
        });
}

class Modal {
        constructor() {
                this.overlay = document.getElementById('new-expense-overlay');
                this.closeButton = document.getElementById('close-modal');
                this.saveButton = document.getElementById('save-expense');

                // Adiciona o listener para fechar o modal
                this.closeButton.addEventListener('click', () => {
                        this.fecharModal();
                });

        }

        abrirModal(id) {
                setModalListeners(id);
                this.overlay.classList.add('show');
        }

        editarModal(despesas, id) {
                document.getElementById('new-expense-year').value = despesas.year;
                document.getElementById('new-expense-month').value = despesas.month;
                document.getElementById('new-expense-day').value = despesas.day;
                document.getElementById('new-expense-type').value = despesas.tipo;
                document.getElementById('new-expense-description').value = despesas.descricao;
                document.getElementById('new-expense-value').value = despesas.valor;

                this.overlay.classList.add('show');
                this.abrirModal(id);

        }

        fecharModal() {
                limparCampos();
                this.overlay.classList.remove('show');
        }
}

// Cria uma instância global do modal
export const modal = new Modal();
