"""Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) uma listagem com as pessoas mais pesadas.
c) Uma listagem com as pessoas mais leves."""

from time import sleep
lista = []
pesadas = []
leves = []
menorPeso = maiorPeso = count = 0

print(f'{"-" * 30}\n {"Pesquisa de peso":^30}\n{"(digite [S] para sair)":^30}\n{"-" * 30}')

while True:

    nome = (str(input(f'Digite o {count+1}º nome: ')).strip().capitalize())

    if nome == 'S':
        break

    peso = (float(input(f'Digite o peso de {nome}: ')))
#  descobrir o menor / maior peso
    if count == 0:
        menorPeso = peso
        maiorPeso = peso
    else:
        if peso <= menorPeso:
            menorPeso = peso
        if peso >= maiorPeso:
            maiorPeso = peso
    lista.append([nome, peso])
    count += 1
#  descobre o nome de quem tem o menor/maior peso
for nome, peso in lista:
    if peso == menorPeso:
        leves.append(nome)
    if peso == maiorPeso:
        pesadas.append(nome)
print('\nFinalizando Cadastro...\n')
sleep(1)
print(f'Foram cadastradas {len(lista)} pessoas.\n'
      f'O menor peso é {menorPeso:.2f} kg, peso de: {", ".join(leves)}.\n'
      f'O maior peso é {maiorPeso:.2f} kg, peso de: {", ".join(pesadas)}.')
