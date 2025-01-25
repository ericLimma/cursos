"""Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
continuar. No final, mostre:
 A) Qual é o total gasto na compra.
 b) quantos produtos custam mais de R$1000.
 c) Qual é o nome do produto mais barato."""

from time import sleep
soma = count = maisCaros = menorPreco = 0
maisBarato = ''

while True:
    produto = str(input('Produto: ')).strip().capitalize()
    preco = float(input('Preço: R$ '))

    if count == 0 or preco < menorPreco:
        maisBarato = produto
        menorPreco = preco

    if preco >= 1000:
        maisCaros += 1

    soma += preco
    count += 1

    continuar = " "
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [s/n] ')).strip().upper()[0]

    if continuar == 'N':
        break

print('\nFinalizando', end='')
sleep(.5)

for c in range(1, 5):
    print('.', end='')
    sleep(.5)
print(f'\nTotal da compra: R$ {soma:.2f}\n'
      f'Produtos mais caros que R$ 1000.00: {maisCaros}\n'
      f'Produto mais barato é o {maisBarato}  que custa {menorPreco}')
print('\nAté logo!')
