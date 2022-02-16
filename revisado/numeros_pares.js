function intervaloPares(inicio, fim, quantidade) {
    let numeros = new Array();
    let numerosPares = new Array;
    let numero = inicio;
    let palavra= "auspicioso"

    for (let i = inicio; i < fim; i++) {
        numero++ ;
        numeros.push(numero);
    }

        numeros.forEach(elemento => {
            if (elemento % 2 === 0)
                numerosPares.push(elemento);
        })
        console.log(numerosPares);    
}
intervaloPares(1, 100, 3);

