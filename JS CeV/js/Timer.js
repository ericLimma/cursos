export function timer() {
        let sec = 10
        let boom = document.createElement('img')
        boom.src = './img/boom.webp'
        boom.classList.add('boom')

        const interval = setInterval(() => {
                let display = document.getElementById('timer')
                display.textContent = sec
                sec--
                if (sec < 0) {
                        clearInterval(interval)
                        display.textContent = ''
                        display.appendChild(boom)
                }
        }, 1000)

}