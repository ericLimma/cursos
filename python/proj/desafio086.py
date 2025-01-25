"""Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
no final mostre a matriz na tela, com a formatação correta"""

matriz = []
row = col = 0

for c in range(1, 4):  # recebe os valores para matriz
    linha = []
    for d in range(1, 4):
        while True:
            n = input('Digite um valor: ')  # impede que seja digitado valor que não seja número
            if n.isnumeric():
                print('adicionado...')
                break
            else:
                print('valor inválido')

        linha.append(n)
    matriz.append(linha)

for linha, valor in enumerate(matriz):
    print(valor)
