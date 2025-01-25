"""Desenvolva um programa que leia o comprimento de três retas e diga ao usário se elas
podem ou não formar um
ex.:
"""

ladoA = float(input('Digite a primeira medida: '))
ladoB = float(input('Digite a segunda medida: '))
ladoC = float(input('Digite a terceira medida: '))

if (ladoA + ladoB > ladoC) and (ladoC + ladoA >ladoB) and (ladoB + ladoC > ladoA):
    print('É um triângulo!')
else:
    print('Não é um triângulo!')