"""Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e
comprimento) e mostre a área do terreno. """


def sep():
    print('-'*20)


def area(larg, comp):
    a = larg * comp
    sep()
    print(f'Largura: {larg} m.\n'
          f'Comprimento: {comp} m.\n'
          f'Área: {a} m²')


area(int(input('Largura: ')), int(input('Comprimento: ')))
