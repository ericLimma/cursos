"""Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia()e somaPar(). A primeira
função vai sortear 5 números e vai colocá-los detro da lista e a segunda função vai mostrar a soma entre todos os
valores PARES sorteados pela função anterior. """
from random import randint

numeros = []
soma = 0


def sorteia():
    while len(numeros) < 5:  # sorteia numeros aleatórios de 0  a 60.
        n = (randint(0, 10))

        if n not in numeros:  # impede que sejam adicionados números repetidos.
            numeros.append(n)
    print(f'Números: {numeros}')


def somapar():
    sorteia()

    global soma
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f'Soma dos pares: {soma}')


somapar()
