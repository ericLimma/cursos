document.addEventListener('DOMContentLoaded', () => {
    const visorDisplay = document.getElementById('display-visor');
    const resultDisplay = document.getElementById('display-result');

    let currentInput = '';
    let previousInput = '';
    let operator = '';
    let result = '';

    function updateVisor() {
        visorDisplay.textContent = currentInput || '0';
        resultDisplay.textContent = result ? `= ${result}` : '';
    }

    function clearCalculator() {
        currentInput = '';
        previousInput = '';
        operator = '';
        result = '';
        updateVisor();
    }

    function calculate() {
        const num1 = parseFloat(previousInput);
        const num2 = parseFloat(currentInput);
        switch (operator) {
            case '+':
                result = num1 + num2;
                break;
            case '-':
                result = num1 - num2;
                break;
            case '*':
                result = num1 * num2;
                break;
            case '/':
                result = num1 / num2;
                break;
            default:
                return;
        }
        currentInput = result.toString();
        operator = '';
        previousInput = '';
    }
    function handleNumberInput(value) {
        if (currentInput.length < 12) {
            if (value === '.' && currentInput.includes('.')) return;
            currentInput += value;
            updateVisor();
        }
    }

    function handleOperatorInput(value) {
        if (currentInput === '' && result !== '') {
            previousInput = result;
        } else {
            previousInput = currentInput;
        }
        currentInput = '';
        operator = value;
        updateVisor();
    }

    function handleEqualInput() {
        if (operator && previousInput && currentInput) {
            calculate();
            updateVisor();
        }
    }

    document.querySelectorAll('.btn-number').forEach(button => {
        button.addEventListener('click', (e) => {
            handleNumberInput(e.target.dataset.value);
        });
    });

    document.querySelectorAll('.btn-operator').forEach(button => {
        button.addEventListener('click', (e) => {
            handleOperatorInput(e.target.dataset.value);
        });
    });

    document.querySelector('.btn-equal').addEventListener('click', () => {
        handleEqualInput();
    });

    document.querySelector('.btn-clear').addEventListener('click', () => {
        clearCalculator();
    });

    clearCalculator(); // Inicializa o visor com o valor zero
})