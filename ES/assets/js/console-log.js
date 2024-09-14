function escrever(text, displayId) {
    const display = document.getElementById(displayId);
    console.log(display)
    display.textContent += text;
}

escrever('Olá, Mundo!', 'display-1');