"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

n = int(input('Digite um número: '))
dividido = 0
lista = []
for c in range (1, n+1):
    if n % c == 0:
        print(f'\33[32m{c}', end= ' ')
        dividido +=1
        lista.append(c)
    else:
        print(f'\33[31m{c}', end= ' ')

print(f'\n\033[mO número foi divido {dividido} vezes,'
      f'pelos números: {lista}')

if dividido > 2:
    print('Por isso ele NÃO É PRIMO')
else:
    print('Por isso ele É PRIMO')