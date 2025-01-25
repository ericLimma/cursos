"""Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""
from time import sleep



def txt():
    sleep(.5)
    print(f'Analisando...')
    sleep(.5)


def maior(*num):
    maxi = 0
    txt()
    for c in num:
        if c > maxi:
            maxi = c
    print(f'O maior número informado foi: {maxi}')


maior(2, 5, 6, 8, 9, 10)
