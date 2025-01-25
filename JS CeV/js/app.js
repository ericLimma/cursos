'use strict'

import { alterarTexto } from './AlterarTexto.js'
import { alterarCorBg } from './AlterarCorBG.js'
import { handleCount } from './HandleCount.js'
import { openModal } from './OpenModal.js'
import { handleDropdown } from './HandleDropdown.js'
import { handleSearch, clearSearchInput } from './HandleSearch.js'
import { openImageModal, closeImageModal } from './ImageModal.js'
import { timer } from './Timer.js'

function setListeners() {
        // Botões gerais
        setupButtons();
        // Campo de busca
        setupSearch();
        // Modal de imagens
        setupImageModal();
        // Outros componentes, se necessário
        setupCharCount()
}

function setupButtons() {
        document.getElementById('btn-1').addEventListener('click', alterarTexto)
        document.getElementById('btn-2').addEventListener('click', alterarCorBg)
        document.getElementById('btn-plus').addEventListener('click', () => { handleCount('plus') })
        document.getElementById('btn-minus').addEventListener('click', () => { handleCount('minus') })
        document.getElementById('open-modal').addEventListener('click', () => { openModal('Olá Mundo!') })
        document.getElementById('dropdown-btn').addEventListener('click', handleDropdown)
        document.getElementById('search-clear-btn').addEventListener('click', clearSearchInput)
        document.getElementById('timer').addEventListener('click', timer)

}

function setupSearch() {
        const searchInput = document.getElementById('fruits-search');
        searchInput.addEventListener('keydown', (event) => {
                if (/^[a-zA-Z]$/.test(event.key) || event.key === 'Backspace') {
                        setTimeout(() => handleSearch(event), 0);
                } else {
                        event.preventDefault();
                }
        });
}

function setupCharCount() {
        const textArea = document.getElementById('textarea');
        const charCount = document.getElementById('char-count');

        // Atualiza o contador sempre que uma tecla é pressionada
        textArea.addEventListener('input', () => {
                const value = textArea.value.length; // Obtém o comprimento do valor atual
                charCount.textContent = value; // Atualiza o contador no DOM
                console.log(value); // Exibe o valor no console
        });
}


function setupImageModal() {
        const imgs = document.querySelectorAll('.imgs img');
        imgs.forEach((img) => img.addEventListener('click', openImageModal));
        document.getElementById('close-img-modal').addEventListener('click', closeImageModal);
}
setListeners()