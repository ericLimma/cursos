import { bd } from "./Bd.js";
import { showAlert } from "./showAlert.js";
import { openModal, modal } from "./modal.js";
import { editarDespesa } from "./cadastrarDespesa.js";

export function carregarListaDespesas(despesas = Array()) {
        if (despesas.length === 0) despesas = bd.recuperarRegistros();

        const listaDespesas = document.getElementById('lista-depesas');
        listaDespesas.innerHTML = '';

        despesas.forEach(despesa => {
                const row = listaDespesas.insertRow();
                const cellDate = row.insertCell(0);
                cellDate.textContent = `${despesa.day.padStart(2, '0')}/${despesa.month.padStart(2, '0')}/${despesa.year}`;

                const cellTipo = row.insertCell(1);
                cellTipo.textContent = getTipoDescricao(despesa.tipo);

                const cellDescricao = row.insertCell(2);
                cellDescricao.textContent = despesa.descricao;

                const cellValor = row.insertCell(3);
                cellValor.textContent = despesa.valor;

                const cellActions = row.insertCell(4); // Adiciona uma célula para os botões de ação
                cellActions.className = 'cell-actions'
                let deleteIcon = '<i class="fa-solid fa-trash-can"></i>';
                let editIcon = '<i class="fa-solid fa-edit"></i>';
                cellActions.append(criarButton('edit', editIcon, despesa.id));
                cellActions.append(criarButton('delete', deleteIcon, despesa.id));
        });
}


function getTipoDescricao(tipo) {
        const tipos = {
                '1': 'Alimentação',
                '2': 'Educação',
                '3': 'Lazer',
                '4': 'Saúde',
                '5': 'Transporte'
        };
        return tipos[tipo] || 'Outro'; // Retorna 'Outro' se o tipo não estiver na lista
}

function criarButton(type, icon, id) {
        let btn = document.createElement('button');
        btn.className = `btn ${type === 'edit' ? 'btn-primary' : 'btn-danger'}`;
        btn.innerHTML = icon;
        btn.id = `despesa-id-${id}`;

        btn.onclick = async function () {
                if (type === 'delete') {
                        const confirmed = await openModal();
                        if (confirmed) {
                                bd.removerDespesa(id);
                                showAlert('success', 'Despesa removida com sucesso');
                                carregarListaDespesas();
                        } else {
                                showAlert('error', 'Ação Cancelada');
                        }
                } else if (type === 'edit') {
                        editarDespesa(id);
                }
        };

        return btn;
}

