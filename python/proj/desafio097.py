"""Faça um programa que tenha uma função chamada escreva(), e receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável.
ex.: escreva('Olá, Mundo!)

saída: --------------------
            Olá Mundo!
       ---------------------"""
titulo = str(input('Digite o título: ')).title()
c = len(titulo)+10


def escreva():
    print(f'{"-"*c}')
    print(f'     {titulo:^}')
    print(f'{"-"*c}')


escreva()
