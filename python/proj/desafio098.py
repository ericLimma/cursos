"""Faça um programa que tenha uma funcao chamada contador(), que receba tres parâmetros: inicio, fim e passo e realize
a contagem. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada."""
from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= (-1)
    elif passo == 0:
        passo = 1

    if inicio < fim:
        while inicio <= fim:
            print(inicio, end=" ")
            inicio += passo
            sleep(.2)
    elif inicio > fim:
        while inicio >= fim:
            print(inicio, end=" ")
            inicio -= passo
            sleep(.2)
    print()


def suavez():

    print('Agora é sua vez! Escolha os numeros: ')
    i = int(input('Inicio: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    contador(i, f, p)


contador(1, 10, 1)
contador(10, 0, 2)
suavez()
