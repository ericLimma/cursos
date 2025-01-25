export function openModal(text) {
        const modal = document.getElementById('modal')

        document.getElementById('modal-text').textContent = text

        modal.classList.remove('d-none');

        document.getElementById('close-modal').addEventListener('click', () => {
                modal.classList.add('d-none')
        })
        setTimeout(() => {
                modal.classList.add('d-none')
        }, 3000)
}
