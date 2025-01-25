"""Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. """

from random import randint

vitorias = 0

while True:
    jogador = ' '
    while jogador not in 'PI':
        jogador = str(input('[P] Par ou [I] Ímpar? ')).strip().upper()[0]  # pega apenas a primeira letra

    dedosJogador = int(input('Digite um número de 0 a 5: '))
    dedosComputador = randint(0, 5)
    perdeu = False
    par = False

    if (dedosJogador + dedosComputador) % 2 == 0:
        par = True
        resultado = 'Par'
    else:
        resultado = "Ímpar"

    if par and jogador == 'I':
        perdeu = True

    if not par and jogador == 'P':
        perdeu = True

    if perdeu:
        break

    print(f'{"-"*40}\n'
          f'Computador escolheu {dedosComputador}, e você {dedosJogador}.\n'
          f'Resultado é {resultado}! Você Ganhou!\n'
          f'{"-"*40}\n')
    vitorias += 1

print(f'{"-"*40}\n'
      f'Computador escolheu {dedosComputador} e você {dedosJogador}.\n'
      f'Resultado é {resultado}! Você perdeu!\n'
      f'Vitórias consecutivas: {vitorias}\n')
