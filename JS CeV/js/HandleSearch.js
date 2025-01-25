const originalList = document.getElementById('fruits-list').innerHTML
const fruitListDisplay = document.getElementById('fruits-list')


export function capitalize(str) {
        return str
                .split(' ')
                .map(word => word.charAt(0).toUpperCase() + word.slice(1))
                .join(' ')
}

export function getFruitsList() {
        const tempDiv = document.createElement('div')
        tempDiv.innerHTML = originalList

        const listItems = Array.from(tempDiv.querySelectorAll('li'))

        const items = Array.from(listItems)
                .map((item) => {
                        return item.textContent
                                .toLowerCase()
                                .normalize("NFD")
                                .replace(/[\u0300-\u036f]/g, "")
                                .replace('ç', 'c');
                });
        return items;
}

export function clearSearchInput() {
        document.getElementById('fruits-search').value = ''
        fruitListDisplay.innerHTML = originalList

}

export function handleSearch(event) {
        const list = getFruitsList();
        let searchChar = event.target.value.toLowerCase()

        const filteredItems = list.filter(item => item.startsWith(searchChar))
        let listToDisplay = '';


        filteredItems.forEach((item) => {
                listToDisplay += `<li>${capitalize(item)}</li>`;
        });

        fruitListDisplay.innerHTML = listToDisplay
}