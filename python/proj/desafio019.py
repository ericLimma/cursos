"""um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um
programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido"""

import random

lista = input('Digite o primeiro nome: '), \
        input('Digite o segundo nome: '), \
        input('Digite o terceiro nome: '), \
        input('Digite o quarto nome: ')

print(f'Os alunos a serem sorteados são: {lista}\n'
      f'O aluno sorteado foi: {random.choice(lista)}')
