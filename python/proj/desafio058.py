"""Melhore o jogo do desafio 028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai
tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer. """
from random import randint
from time import sleep


jogador = int(input('Adivinhe o número que estou pensando de 0 a 5: '))
computador = randint(0, 5)
contador = 1
if jogador != computador:
    while jogador != computador:
        jogador = int(input('tente novamente: '))
        contador += 1

print(f'Você acertou! Computador: {computador}, Jogador: {jogador}.\n'
      f'Você acertou na {contador}ª tentativa!')
