import { Despesa } from "./Despesa.js";
import { bd } from "./Bd.js";
import { carregarListaDespesas } from "./carregarListaDespesas.js";

export function pesquisarDespesa() {
        const year = document.getElementById('year').value;
        const month = document.getElementById('month').value;
        const day = document.getElementById('day').value;
        const tipo = document.getElementById('tipo').value;
        const descricao = document.getElementById('descricao').value;
        const valor = document.getElementById('valor').value;

        const despesa = new Despesa(year, month, day, tipo, descricao, valor);

        let despesas = bd.pesquisar(despesa);
        carregarListaDespesas(despesas);
}
