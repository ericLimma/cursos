const sorvetes = new Array(
  "\nMilho Verde",
  "\nChocolate",
  "\nMorango",
  "\nLeite Condensado",
);
const sopas = new Array(
  "\nFrango",
  "\nLegumes",
  "\nCarne",
  "\nFeijão"
);
const pratosTradiocionais = new Array(
  "\nFrango Grelhado",
  "\nBife Acebolado",
  "\nOvos Mexidos",
  "\nFilé á Parmegiana",
);
const cafeVerao = new Array(
  "\nOvos Mexidos",
  "\nBacon",
  "\nTorradas",
  "\nFrutas"
);
const cafeInverno = new Array(
  "\ncansei 1",
  "\ncansei 2",
  "\ncansei 3",
  "\ncansei 4",
)


const temperatura = 33;
const calor = temperatura > 28;
const frio = temperatura < 19;
const hora = 10;
const manha = hora < 11;
const tarde = hora >= 11;
const noite = hora >= 18;
let temNoCardapio = false;


if (calor) {

  if (manha && calor) {
    console.log(`Confira nossas opções de café da manhã de verão:\n` + cafeVerao);
  } else {
    console.log(`Está calor hoje, que tal um sorvete?\nConfira os sabores:\n` + sorvetes);
  }

} else if (frio) {

  if (manha && frio) {
    console.log(`Confira nossas opções de café da manhã de inverno: \n` + cafeInverno);
  } else {
    console.log(`Está frio hoje, que tal uma sopa?\nConfira os sabores:\n` + sopas);
  }

} else {
  console.log(`Confira nossos pratos tradicionais:\n` + pratosTradiocionais);
}

const escolha = " Torradas";

for (let i = 0; i < sorvetes.length; i++) {

  if (escolha == sorvetes[i] || escolha == sopas[i] || escolha == pratosTradiocionais[i] || escolha == cafeVerao[i] || escolha == cafeInverno[i]) {
    temNoCardapio = true;
  }
}

if (temNoCardapio == true) {
  console.log("\nSeu pedido estará pronto em um minuto");
} else {
  console.log("\nDesculpe, não temos isso em nosso cardápio");
}