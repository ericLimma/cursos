const imgModal = document.getElementById('img-modal')
const imgModalOverlay = document.getElementById('img-modal-overlay')
const modalDisplay = document.getElementById('modal-display')

export function openImageModal(event) {
        imgModal.classList.add('show')
        imgModalOverlay.classList.add('show')
        modalDisplay.src = event.target.src

}
export function closeImageModal() {
        imgModal.classList.remove('show')
        imgModalOverlay.classList.remove('show')
        modalDisplay.src = ''
}