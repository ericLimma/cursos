export class Bd {
        constructor() {
                let id = localStorage.getItem('id');
                if (id === null) {
                        localStorage.setItem('id', 0);
                }
        }

        getNextId() {
                let nextId = parseInt(localStorage.getItem('id')) + 1;
                return nextId;
        }

        gravar(despesa, id = null) {
                if (id === null) {
                        // Novo registro
                        id = this.getNextId();
                }

                localStorage.setItem(id, JSON.stringify(despesa));
                if (id > parseInt(localStorage.getItem('id'))) {
                        localStorage.setItem('id', id);
                }
        }

        recuperarRegistros() {
                let id = localStorage.getItem('id');
                let despesas = [];
                for (let i = 1; i <= id; i++) {
                        let despesa = JSON.parse(localStorage.getItem(i));
                        if (despesa === null) {
                                continue;
                        }
                        despesa.id = i;
                        despesas.push(despesa);
                }
                return despesas;
        }


        pesquisar(despesa) {
                let despesasFiltradas = Array();
                despesasFiltradas = this.recuperarRegistros();

                if (despesa.year != '') {
                        despesasFiltradas = despesasFiltradas.filter(d => d.year == despesa.year);
                }
                if (despesa.month != '') {
                        despesasFiltradas = despesasFiltradas.filter(d => d.month == despesa.month);
                }
                if (despesa.day != '') {
                        despesasFiltradas = despesasFiltradas.filter(d => d.day == despesa.day);
                }
                if (despesa.tipo != '') {
                        despesasFiltradas = despesasFiltradas.filter(d => d.tipo == despesa.tipo);
                }
                if (despesa.descricao != '') {
                        despesasFiltradas = despesasFiltradas.filter(d => d.descricao == despesa.descricao);
                }
                if (despesa.valor != '') {
                        despesasFiltradas = despesasFiltradas.filter(d => d.valor == despesa.valor);
                }

                return despesasFiltradas;
        }
        removerDespesa(id) {
                localStorage.removeItem(id);
        }

        recuperarPorId(id) {
                let despesaRecuperada = JSON.parse(localStorage.getItem(id));
                return despesaRecuperada;
        }

}

export const bd = new Bd;