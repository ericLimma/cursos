"""Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente. """

numeros = [[], []]  # ou numeros = [[], []]

for c in range(0, 7):
    num = ''
    while not num.isnumeric():  # impede que seja digitado algo que não seja número
        num = input('Digite um número: ')
    num = int(num)
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

print(f'Pares: {sorted(numeros[0])}\n'
      f'Impares: {sorted(numeros[1])}\n')
