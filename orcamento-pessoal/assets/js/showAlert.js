export function showAlert(typeAlert, text) {

        let alert = document.createElement('div');
        let className = '';
        let icon = '';

        // Define o ícone e a classe com base no tipo de alerta
        switch (typeAlert) {
                case 'success':
                        icon = `<i class="fa-solid fa-circle-check"></i>`;
                        className = 'alert text-white bg-success show';
                        break;
                case 'error':
                        icon = `<i class="fa-solid fa-circle-xmark"></i>`;
                        className = 'alert text-white bg-danger show';
                        break;
                case 'warning':
                        icon = `<i class="fa-solid fa-circle-exclamation"></i>`;
                        className = 'alert bg-warning show';
                        break;
                default:
                        className = 'alert';
                        break;
        }

        // Define o conteúdo e a classe do alerta
        alert.innerHTML = `${icon} ${text}`;
        alert.className = className;

        // Adiciona o alerta ao DOM
        document.body.appendChild(alert);

        // Força uma re-renderização para aplicar as classes
        void alert.offsetWidth; // Pode ser usado para forçar a re-renderização

        // Remove o alerta após 3 segundos
        setTimeout(() => {
                document.body.removeChild(alert);
        }, 3000);

};
