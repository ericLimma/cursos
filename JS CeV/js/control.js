document.addEventListener('DOMContentLoaded', () => {
        const body = document.getElementById("body");

        // Dimensões do viewport
        const viewportWidth = window.innerWidth;
        const viewportHeight = window.innerHeight;

        // Tamanho de cada quadrado
        const squareSize = Math.max(0.05 * viewportWidth, 50); // 5% do viewport ou no mínimo 50px
        const gapSize = 8; // Gap de 1rem em pixels (ajuste conforme necessário)

        // Quantidade de quadrados que cabem na tela (considerando o gap)
        const squaresPerRow = Math.floor((viewportWidth + gapSize) / (squareSize + gapSize));
        const squaresPerColumn = Math.floor((viewportHeight + gapSize) / (squareSize + gapSize));

        // Total de quadrados
        const totalSquares = squaresPerRow * squaresPerColumn;
        const squaresList = []

        // Adiciona os quadrados ao body
        for (let i = 0; i < totalSquares; i++) {
                const square = document.createElement('div');
                square.classList.add('square');
                square.style.width = `${squareSize}px`;
                square.style.height = `${squareSize}px`;
                body.appendChild(square);
                squaresList.push(square)

        }
        function getRandomIndex(arr) {
                const timestamp = Date.now();  // Timestamp atual em milissegundos
                return timestamp % arr.length;  // Usa o timestamp como índice
        }

        const interval = setInterval(() => {
                const randomIndex = getRandomIndex(squaresList);
                squaresList[randomIndex].style.opacity = '0'
                squaresList.splice(randomIndex, 1)

                if (squaresList.length == 0) {
                        clearInterval(interval)
                        console.log('BOOOM')
                }
        }, 1000)

});

window.addEventListener('resize', () => {
        location.reload(); // Simples, recarrega a página ao redimensionar
});