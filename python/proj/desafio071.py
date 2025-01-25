"""Crie um programa que simule o funcionamento de um caixa eletrônico.; No início, pergunte ao usuário qual será o
valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS.: Considere que o caixa possui apenas cédulas de R$ 50, R$20, R$ 10, e R$1"""

continuar = 'S'

while continuar == 'S':

    nota1 = nota10 = nota20 = nota50 = 0
    valorSacado = int(input('Qual o valor a ser sacado? '))

    while valorSacado >= 50:
        valorSacado -= 50
        nota50 += 1

    while valorSacado >= 20:
        valorSacado -= 20
        nota20 += 1

    while valorSacado >= 10:
        valorSacado -= 10
        nota10 += 1

    while valorSacado >= 1:
        valorSacado -= 1
        nota1 += 1

    print(f'Notas de R$ 50: {nota50}\n'
          f'Notas de R$ 20: {nota20}\n'
          f'Notas de R$ 10: {nota10}\n'
          f'Notas de R$ 1:  {nota1}\n')

    continuar = str(input('Deseja repetir? [s/n] ')).strip().upper()

print('Até logo!')