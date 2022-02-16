let num = new Array();
let valor = 0;

function contar() {
    for (let i = 0; i < 15; i++) {
        valor++;
        num.push(valor);
        console.log(valor);
    }
}
contar();
//console.log(valor);
//console.log(num);