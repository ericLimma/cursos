"""Crie um programa que leia o nome completo de uma pessoa e mostre:
 - O nome com todas as letras maiúsculas;
 - O nome com todas as letras minúsculas;
 - Quantas letras ao todo sem considerar os espaços;
 - Quantas letras tem o primeiro nome."""

nome = str(input('Digite o nome completo: ')).strip()
dividido = nome.split()
# quantidadeCaracteres = len(nome) - nome.count(' ') - Solução 1
print(f'Com letras maiúsculas: {nome.upper()}\n'
      f'Com letras minúsculas: {nome.lower()}\n'
      # f'Total de letras sem espaço: {quantidadeCaracteres}\n' - Solução 1
      f'Total de letras sem espaço: {len(nome.replace(" ", ""))}\n'  # Solução 2
      f'Quantas letras tem o primeiro nome: {len(dividido[0])}.')
