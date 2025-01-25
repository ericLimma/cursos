"""Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome,
em qualquer lugar do nome"""

nome = str(input('Digite seu nome: ')).strip()

if nome.upper().count("SILVA") == 1:
    print('Seu nome tem Silva')
else:
    print('Seu nome não tem Silva')
