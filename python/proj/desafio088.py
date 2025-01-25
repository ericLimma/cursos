"""Faça um programa que me ajude um jogador a ganhar na MEGA SENA a criar palpites. O programa vai perguntar quantos
jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta """

from time import sleep
from random import randint

print(f'{"-"*30}\n'
      f'{"Números de Loteria":^30}\n'
      f'{"-"*30}')
jogos = []
while True:
    qnt = input('Quantas apostas você quer fazer: ').strip()
    if qnt.isnumeric():
        qnt = int(qnt)
        if qnt > 0:
            break
        else:
            print('\33[31mOpção Inválida, digite novamente...\33[m ')
    else:
        print('\33[31mOpção Inválida, digite novamente...\33[m ')
print("\33[32mInicializando programa...\33[m")

for c in range(1, qnt+1):
    count = 1
    jogo = []

    while count < 7:
        numero = randint(1, 60)

        if numero not in jogo:
            jogo.append(numero)
            count += 1

    jogos.append(sorted(jogo))


for i, jogo in enumerate(jogos):
    print(f'\nJogo Nº{i+1:>2}: ', end='')
    for numero in jogo:
        print(f'{numero:^2}', end=" ")
print()
