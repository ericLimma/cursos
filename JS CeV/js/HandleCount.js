export function handleCount(operator) {

        let count = document.getElementById('count-1')
        let num = Number(count.textContent)

        if (operator === 'plus') {
                num += 1
        } else {
                num -= 1
        }
        count.textContent = num
}