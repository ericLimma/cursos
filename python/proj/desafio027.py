"""Faça um programa que leia o nome completo de uma pessoa, mostranddo em seguida o
primeiro e o último nome separadamente.

ex.: Ana Maria de Souza
Primeiro = Ana
último = Souza"""

nome = str(input('Digite seu nome completo: ')).strip().title().split()


"""dividido = nome
print(f'Primeiro nome: {dividido[0]}\n'
      f'Último nome: {dividido[-1]}\n')"""


print(f'Primeiro nome: {nome[0]}\n'
      f'Último nome: {nome[-1]}\n')
