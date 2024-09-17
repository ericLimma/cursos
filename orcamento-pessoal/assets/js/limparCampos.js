export function limparCampos() {

        const campos = document.querySelectorAll('.form-control, .form-select');
        campos.forEach(campo => campo.value = '')

}
