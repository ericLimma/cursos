"""Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualiza
de detalhes do aproveitamento de cada jogador"""
from time import sleep
jogadores = dict()

while True:
    nome = str(input('Nome do jogador: ')).capitalize()
    nPartidas = int(input(f'Quantos jogos {nome} jogou? '))
    gols = []
    jogadores['total'] = 0

    for c in range(1, nPartidas + 1):
        g = str(input(f'Quantos gols {nome} fez na {c}ª partida? '))
        gols.append(g)
        jogadores['total'] += g

    jogadores[nome] = gols

    sair = str(input('Deseja sair? [s/n] '))[0].upper()
    if sair == 'S':
        break
print(jogadores)