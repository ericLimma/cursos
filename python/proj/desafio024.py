"""Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o
nome SANTO."""

cidade = str(input('\nDigite sua cidade: ')).strip()

if cidade.upper().count('SANTO') == 1:
    print('\nSua cidade começa com "Santo"')
else:
    print('\nSua cidade não começa com "Santo"')
