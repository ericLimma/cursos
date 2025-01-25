"""Faça um programa que leia o peso de cinco pessoas. no final, mostre qual foi o maior
e o menores pesos lidos"""
menorPeso = 0
maiorPeso = 0
for c in range(1, 6):
    peso = float(input(f'Digite {c}º peso em kg: '))
    if c == 1:
        menorPeso = peso
        maiorPeso = peso
    else:
        if peso < menorPeso:
            menorPeso = peso
        if peso > maiorPeso:
            maiorPeso = peso
print(f'O menor peso é: {menorPeso:.2f} kg.\n'
      f'O maior peso é: {maiorPeso:.2f} kg')
