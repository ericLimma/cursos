document.addEventListener('DOMContentLoaded', () => {
    let inputs = document.querySelectorAll('#email, #senha'); // Seleciona ambos os elementos

    const evitarEspacos = (input) => {
        let posicaoCursor = input.selectionStart; // Captura a posição do cursor
        input.value = input.value.replace(/\s/g, ''); // Remove espaços
        input.setSelectionRange(posicaoCursor, posicaoCursor); // Restaura a posição do cursor
    };

    const adicionarClasseErro = () => {
        const params = new URLSearchParams(window.location.search);
        if (params.get('login') === 'error') {
            inputs.forEach((input) => {
                input.classList.add('is-invalid'); // Adiciona a classe 'is-invalid' (erro visual)
            });
        }
    };

    adicionarClasseErro();

    inputs.forEach((input) => {
        input.addEventListener('input', () => {
            evitarEspacos(input); // Passa o próprio input
        });
    });
});
