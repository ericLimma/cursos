import { showAlert } from "./showAlert.js";
import { Despesa } from "./Despesa.js";
import { bd } from "./Bd.js";
import { limparCampos } from "./limparCampos.js";
import { carregarListaDespesas } from "./carregarListaDespesas.js";
import { modal } from "./modal.js";

let despesaEditandoId = null; // Flag para identificar se é edição ou novo cadastro

// Função para abrir o modal para adicionar uma nova despesa
export function abrirModalParaAdicionar() {
        // Limpa os campos do modal
        limparCampos();
        // Fecha o modal, se estiver aberto
        modal.fecharModal();
        // Define a flag de edição como nula para garantir que estamos adicionando
        despesaEditandoId = null;
        // Abre o modal
        modal.abrirModal();
}

// Função para cadastrar ou atualizar uma despesa
export function cadastrarDespesa(id) {
        let year = document.getElementById('new-expense-year').value;
        let month = document.getElementById('new-expense-month').value;
        let day = document.getElementById('new-expense-day').value;
        let tipo = document.getElementById('new-expense-type').value;
        let descricao = capitalizeFirstLetter(document.getElementById('new-expense-description').value.trim());
        let valor = document.getElementById('new-expense-value').value;

        let despesa = new Despesa(year, month, day, tipo, descricao, valor);

        if (despesa.validarDados()) {
                if (id) {
                        // Lógica de edição
                        despesa.id = id; // Defina o ID para a despesa existente
                        bd.gravar(despesa, id); // Atualiza a despesa existente
                        showAlert('success', 'Despesa editada com sucesso');
                } else {
                        // Lógica de nova despesa
                        bd.gravar(despesa); // Adiciona a nova despesa
                        showAlert('success', 'Despesa salva com sucesso');
                }

                // Fechar o modal, atualizar a lista de despesas e limpar os campos
                modal.fecharModal();
                carregarListaDespesas();
                limparCampos();
        } else {
                showAlert('error', 'Dados incompletos ou inválidos');
        }
}



export function editarDespesa(id) {
        let despesas = bd.recuperarPorId(id);
        modal.editarModal(despesas, id);
}

// Função para capitalizar a primeira letra da string
function capitalizeFirstLetter(str) {
        return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}
