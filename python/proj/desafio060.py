"""Faça um programa que leia um número qualquer e mostre seu fatorial.
ex.: 5! = 5 x 4 x 3 x 2 x1 = 120 """

num = int(input('Digite um número: '))
resultado = 1

if num >= 1:
    print(f'{num}! = ', end='')
    c = num
    while c > 0:
        if c > 1:
            print(f'{c} x ', end='')
        else:
            print(f'{c} ', end='')
        resultado *= c
        c -= 1

    print(f'= {resultado}')

if num < 1:
    print('Digite um valor inteiro maior que 0!')
