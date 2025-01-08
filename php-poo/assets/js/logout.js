// Função para criar e mostrar o modal
function criarModal() {
        let modal = document.createElement('div');
        modal.id = 'logout-modal';
        modal.className = 'modal';

        modal.innerHTML = `
            <div class='modal-content bg-dark text-light'>
                <span class='close' id='close-modal'>&times;</span>
                <h2>Confirmar Logout</h2>
                <p>Você tem certeza que deseja sair?</p>
                <button class='btn btn-danger' id="confirm-logout">Sim, sair</button>
                <button class='btn btn-light mt-3' id="cancel-logout">Cancelar</button>
            </div>
        `;

        // Adiciona o modal ao body
        document.body.appendChild(modal);

        // Agora que o modal está no DOM, podemos adicionar os event listeners

        // Função para fechar o modal
        document.getElementById('close-modal').addEventListener('click', () => {
                document.getElementById('logout-modal').style.display = 'none';
                document.body.removeChild(modal); // Remove o modal do DOM
        });

        // Função para cancelar o logout
        document.getElementById('cancel-logout').addEventListener('click', () => {
                document.getElementById('logout-modal').style.display = 'none';
                document.body.removeChild(modal); // Remove o modal do DOM
        });

        // Função para confirmar o logout
        document.getElementById('confirm-logout').addEventListener('click', () => {
                fetch('../../includes/logout.php', {
                        method: 'POST' // ou 'GET', dependendo de como você quer enviar a requisição
                })
                        .then(response => {
                                if (response.ok) {
                                        // Redirecionar ou fazer algo após o logout
                                        window.location.href = '../../index.php'; // Redireciona para a página de login
                                } else {
                                        alert('Erro ao realizar logout');
                                }
                        })
                        .catch(error => {
                                console.error('Erro:', error);
                        });

                // Fecha o modal após confirmar logout
                document.getElementById('logout-modal').style.display = 'none';
                document.body.removeChild(modal); // Remove o modal do DOM
        });
}

// Event listener para o botão de logout
document.getElementById('logout-button').addEventListener('click', () => {
        criarModal(); // Chama a função para criar e mostrar o modal
        document.getElementById('logout-modal').style.display = 'flex'; // Exibe o modal
});
