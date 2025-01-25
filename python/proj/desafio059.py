"""Crie um programa que leia dois valores e mostre um menu na tela
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

seu programa deverá realizar a operação solicitada em cada caso."""
from time import sleep
num1 = ''
num2 = ''
opcao = 4

while opcao != 5:
    if opcao == 4:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
    opcao = int(input('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    Opção: '''))
    if opcao == 1:
        print(f'Resultado: {num1 + num2}')
    elif opcao == 2:
        print(f'Resultado: {num1 * num2}')
    elif opcao == 3:
        lista = [num1, num2]
        listaClass = sorted(lista)[1]
        print(f'Resultado: {listaClass}')
    elif opcao == 5:
        print(f'Finalizando...')
        sleep(.5)
    else:
        print('Opção inválida')

print('Até mais!')
