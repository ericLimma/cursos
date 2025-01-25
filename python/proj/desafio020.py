"""o professor quer sortear a ordem ded apresentação de trabalhos dos alunos. Faça um
programa que leia o nome dos quatro alunos e moste a ordem sorteada."""

from random import shuffle
lista = [input('Digite o nome do primeiro aluno: '),
         input('Digite o nome do segundo aluno: '),
         input('Digite o nome do terceiro aluno: '),
         input('Digite o nome do quarto aluno: ')]

shuffle(lista)

print('\nA Ordem de apresentação é: {}'.format((', '.join(lista))))
