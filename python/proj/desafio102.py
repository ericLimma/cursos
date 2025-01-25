"""Desafio 102 - Crie  um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique
o número a calcular e o outro chamado show, que será uma valor lógico(opcional) indicando se será mostrado ou não na
tela o processo de cálculo do fatorial. """


def fatorial(num=1, show=False):
    f = 1

    for c in range(1, num + 1):
        f *= c
        if show:
            print(f, end=' ')
    if not show:
        print(f'Resultado: {f}')
    print('FIM!')


fatorial(5, True)
