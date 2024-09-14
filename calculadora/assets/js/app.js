let displayVisor = document.getElementById("display-visor");
let displayResult = document.getElementById("display-result");
let isFirstDigit = true;
let isFirstComma = true;
let currentOperation = '';
let result = 0;
let lastOperator;
let lastDigit;

function clearVisor() {
    displayVisor.innerHTML = '';
    displayResult.innerHTML = '';
    isFirstDigit = true; 
    isFirstComma = true;
    currentOperation = '';
    result = 0;
}

function handleAdiction(value) {
    result += parseFloat(currentOperation || 0);
    currentOperation = ''
    displayResult.innerHTML = `= ${result}`;
    lastOperator = '+'

}

function handleSubtraction() {
    result -= parseFloat(currentOperation || 0);
    currentOperation = ''
    displayResult.innerHTML = `= ${result}`;
    lastOperator = '-'
}
function handleSquare() {
    currentOperation = Math.pow(parseFloat(currentOperation), 2);
    displayResult.innerHTML = `= ${currentOperation}`;
}
function handleSquareRoot() {
    currentOperation = Math.sqrt(parseFloat(currentOperation));
    displayResult.innerHTML = `= ${currentOperation}`;
}

function handlePercent() {
    currentOperation = parseFloat(currentOperation) / 100;
    displayResult.innerHTML = `= ${currentOperation}`;
}

function handleDivide() {
    result /= parseFloat(currentOperation || 1);
    currentOperation = '';
    displayResult.innerHTML = `= ${result}`;
    lastOperator = '/';
}

function handleMultiplication() {
    result *= parseFloat(currentOperation || 1);
    currentOperation = '';
    displayResult.innerHTML = `= ${result}`;
    lastOperator = '*';
}


function calculateResult() {
    switch (lastOperator) {
        case '+':
            handleAddition();
            break;
        case '-':
            handleSubtraction();
            break;
        case '/':
            handleDivide();
            break;
        case '*':
            handleMultiplication();
            break;
    }
}

function showDisplay(currentOperation) {
    displayVisor.innerHTML = ''; // Clear existing content
    for (let char of currentOperation) {
        displayVisor.innerHTML += `<div>${char}</div>`;
    }
}

function getValue(value, type) {
    if (type === "number") {
        if (isFirstDigit) {
            if (value === '0') {
                value = ""
                return;
            }
        }
        if (value === ',') {
            if (isFirstComma) {
                if (isFirstDigit) {
                    value = '0.'
                }
                value = '.';
                isFirstComma = false;
            } else {
                value = ''
            }
        }
        currentOperation += value;
        displayResult.innerHTML = `= ${result}`;
        isFirstDigit = false;
        lastDigit = 'number';
    }

    if (type === "operator") {
        if (lastDigit === 'number') {
            calculateResult
        }
        operation(value);
        isFirstComma = true;
    }
    showDisplay(currentOperation, value);
} 
