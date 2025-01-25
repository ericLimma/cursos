export function sendForm(event) {
        event.preventDefault();

        const inputList = document.querySelectorAll('#form .input')

        inputList.forEach((input) => {
                if (input.value == '') {
                        input.classList.add('border-danger')
                        openModal('Texto faltante!')
                }
        })
}
