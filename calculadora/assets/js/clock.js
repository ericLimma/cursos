function formatTime(date) {
    const hours = date.getHours().toString().padStart(2, '0');
    const minutes = date.getMinutes().toString().padStart(2, '0');
    return `${hours}:${minutes}`;
}

// Função para atualizar o relógio no HTML
function updateClock() {
    const now = new Date();
    const timeString = formatTime(now);
    document.getElementById('clock').textContent = timeString;
}

// Atualizar o relógio imediatamente e a cada segundo
updateClock();
setInterval(updateClock, 1000);