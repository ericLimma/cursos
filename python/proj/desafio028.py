"""Escreva um programa que faça o computador "pensar" em um número entre 0 e 5 e peça
para o usuário tentar descobrir qual foi o número escolhido pelo computador.
 - o programa deverá escrever na tela se o usuário venceu ou perdeu"""

#usar random choice
from random import choice, randint
from time import sleep

num = int(input('Adivinhe o número de 0 a 5: '))
#  numeros = [1,2,3,4,5] - minha solução
computador = randint(0, 5)  # sorteia um número entre 0 e 5

#numeroSorteado = choice(numeros)
print('Processando....')
sleep(2)
#if num == numeroSorteado:
if num == computador:
    print('Você acertou!!')
else:
    # print(f'Você errou! Eu pensei no número {numeroSorteado}')
    print(f'Você errou! Eu pensei no número {computador}')