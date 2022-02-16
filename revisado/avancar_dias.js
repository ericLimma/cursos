function avancarDias(dia, quantidade) {


  const dias = ["Segunda-feira", "Terca-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado", "Domingo"];
  
  
  let posicao = 0;
  let posicaoAtual = dias.indexOf(dia);
  let respost= `${dias[posicao]} ${posicaoAtual}`;

  if (quantidade > 7) {
    posicao = ((posicaoAtual + quantidade) % 7);
  } else {
    posicao = (posicaoAtual + quantidade);
  }

  return respost;
}
avancarDias("Terca-feira", 8);