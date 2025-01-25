'''crie um programa que leia um numero real qualquer pelo  teclado e mostre na tela a
suia porção inteira
 ex.: Digite um número: 6.127, o numero 6.127 tem a parte  inteira 6
 --usar modulo math'''


import math

num = float(input('Digite um número decimal: '))

# print(math.floor(num)) jeito errado
print(f'{math.trunc(num)}') # jeito certo
