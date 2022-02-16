function contaLetras(palavra, letra) {

	let contador = 0;
	for (let i = 0; i < palavra.length; i++) {
			if (palavra[i] == letra) {
				contador++;
			}
		}
	console.log(contador);
}
contaLetras("azul", "a");