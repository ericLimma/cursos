"""Escreva um programa que leia o salário de um funcionário e calcule o valor de seu
aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
"""

salario = float(input('Digite seu salário: '))

if salario <= 1250 :
    print(f'Seu novo salário é: {salario + (salario * 0.15):.2f}')
else:
    print(f'Seu novo salário é: { salario+(salario*.1):.2f}')