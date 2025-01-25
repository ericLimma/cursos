"""Crie um programa que faça o computador jogar jokenpô com você"""
from random import randint
from time import sleep
jogador = int(input('''Vamos jogar? Suas Opções:
[1] Papel
[2] Pedra
[3] Tesoura
Qual sua jogada? '''))
computador = randint(1,3)

if jogador == 1 or jogador == 2 or jogador ==3:
    print('JO')
    sleep(.5)# faz o computador aguarda 1 segundo
    print('KEN')
    sleep(.5)
    print('PÔ')
    sleep(.5)
    if jogador == 1:
        if computador == 1:
            print('Empate, nós dois escolhemos papel')
        elif computador == 2:
            print('Eu venci, papel vence pedra')
        elif computador == 3:
            print('Você venceu, tesoura vence papel')

    elif jogador == 2:
        if computador == 1:
            print('Você venceu, papel derrota pedra')
        elif computador == 2:
            print('Empate, nós dois escolhermos pedra')
        elif computador == 3:
            print('Eu venci, pedra vence tesoura')
    elif jogador == 3:
         if computador == 1:
             print('Eu venci, tesoura vence papel')
         elif computador == 2:
             print('Você venceu, pedra vence tesoura')
         elif computador == 3:
             print('Empate, nós dois escolhemos tesoura')
else:
    print('Jogada inválida')