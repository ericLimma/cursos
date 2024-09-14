let visorDisplay = document.getElementById('display-visor');
let resultDisplay = document.getElementById('display-result');

let expression = ''; // Armazena a expressão completa
let currentNumber = ''; // Armazena o número atual digitado
let result = 0;  // Armazena o resultado da operação
let countNum = 0;
let lastOperator = null; // Armazena o último operador clicado
let isFirstDigit = true;
let isFirstDot = true; // Indica se já foi inserido um ponto no número
let lastCharacterType = 'none'; // Tipo do último caractere ('number' ou 'operator')

function getValue(value, type) {
    if (type === 'number') {
        handlNumber(value)
    }

    if (type === 'operator') {
        handleOperator(value); // Usa a função separada para lidar com operadores
    }

    if (type === 'functionKey') {
        handleFunctionKey(value)
    }

    visorDisplay.innerHTML = expression; // Exibe a expressão completa
    resultDisplay.innerHTML = result ? `= ${result}` : ''; // Exibe o resultado
}
function handlNumber(value) {
    if (isFirstDigit && lastOperator === null) {
        expression = '';
    }
    if (isFirstDigit && value === '0' && currentNumber === '') { // Impede que seja exibido 0123, por exemplo
        return;
    }
    if (isFirstDigit && value === '.') {
        value = '0.'; // Se o usuário tentar começar com um ponto decimal
        isFirstDot = false;
    }
    if (!isFirstDot && value === '.') {
        return; // Impede a inserção de mais de um ponto decimal no mesmo número
    }
    if (countNum === 12) { // Limita o número de dígitos
        return;
    }
    if (value === '.') {
        isFirstDot = false; // Desativa a possibilidade de inserir outro ponto decimal
    }
    currentNumber += value; // Acumula o valor digitado para operação
    expression += value; // Concatena o valor digitado para exibição
    isFirstDigit = false; // Muda o status, liberando o 0
    countNum++;
    lastCharacterType = 'number'
}
function handleOperator(operator) {
    if (lastCharacterType == 'operator') {
        
    }
    if (lastOperator) {
        result = operate(result, parseFloat(currentNumber), lastOperator);
    } else {
        result = parseFloat(currentNumber); // Primeira operação
    }
    expression += ` ${operator} `; // Adiciona o operador à expressão
    currentNumber = ''; // Reseta o número atual
    lastOperator = operator; // Atualiza o último operador
    isFirstDigit = true;
    isFirstDot = true;
    countNum = 0;
    lastCharacterType = 'operator'
}

function operate(result, currentNumber, operator) {
    switch (operator) {
        case '+':
            return result + currentNumber;
        case '-':
            return result - currentNumber;
        case '*':
            return result * currentNumber;
        case '/':
            return result / currentNumber;
        default:
            return currentNumber;
    }
}
function handleFunctionKey(functionKey) {
    switch (functionKey) {
        case 'clear':
            clearAll();
            break;
        case '=':
            equal();
            break;
        case 'back-space':
            backSpace();
            break;
    }
}

function clearAll() {
    expression = '';
    currentNumber = '';
    result = 0;
    countNum = 0;
    isFirstDigit = true;
    isFirstDot = true;
    lastOperator = null;
    visorDisplay.innerHTML = '0';
    resultDisplay.innerHTML = '';
}

function backSpace() {
    if (currentNumber !== '') {
        // Remova o último caractere do número atual
        currentNumber = currentNumber.slice(0, -1);

        // Ajuste o contador de dígitos
        countNum--;

        // Verifique se o ponto foi removido
        if (currentNumber.indexOf('.') === -1) {
            isFirstDot = true;
        }

        // Se o número atual ficar vazio, reinicie as variáveis relevantes
        if (currentNumber === '') {
            isFirstDigit = true;
            countNum = 0;
        }

        // Remova o último caractere da expressão
        expression = expression.slice(0, -1);
    } else if (expression !== '' && lastCharacterType === 'operator') {
        // Remova o operador da expressão
        expression = expression.slice(0, -3); // Remove " operador "
        lastOperator = null;
        lastCharacterType = 'number'; // Prepara para a próxima entrada ser um número
    }

    // Atualize o visor com os valores modificados
    visorDisplay.innerHTML = expression || '0'; // Mostra 0 se a expressão estiver vazia
}