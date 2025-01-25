"""Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna
C) O maior valor da segunda linha """

matriz = []
soma = col3 = 0
for a in range(1, 4):

    linha = []
    for b in range(1, 4):

        while True:

            n = input('Digite um número: ')  # impede que seja digitado valor que não seja número
            if n.isnumeric():
                print('\33[32mValor adicionado...\33[m')
                break
            else:
                print('\33[31mValor inválido, tente novamente...\33[m')

        linha.append(int(n))
    matriz.append(linha)

for linha in matriz:  # mostra a matriz

    for coluna, valor in enumerate(linha):  # mostra os valores linha por linha
        print(valor, end=' ')
        soma += valor  # soma todos os valores

        if coluna == 2:  # soma os valores da coluna 2
            col3 += valor
    print()

print(f'A soma de todos os valores é: {soma}\n'
      f'A soma dos valores da coluna 3 é: {col3}\n'
      f'O maior valor da segunda linha é: {max(matriz[1])}')
