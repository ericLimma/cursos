export class Despesa {

        constructor(year, month, day, tipo, descricao, valor) {
                this.year = year;
                this.month = month;
                this.day = day;
                this.tipo = tipo;
                this.descricao = descricao;
                this.valor = valor;
        };

        validarDados() {
                for (let i in this) {
                        if (this[i] == undefined || this[i] == '' || this[i] == null) {
                                return false;
                        }
                }
                return true;
        }
};
