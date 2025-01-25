export function alterarCorBg() {

        const randomColor = `#${Math.floor(Math.random() * 16777215).toString(16)}`
        console.log(randomColor)

        const body = document.body
        body.style.backgroundColor = `${randomColor}`

        setTimeout(() => {
                body.style.backgroundColor = `#f5f5dc`
        }, 1000);
}