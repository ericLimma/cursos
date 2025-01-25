"""Escreva um programa para aprovar empréstimo bancário para a comrpra de uma casa. O
programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele
vai pagar.
Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou
então o empréstimo será negado."""

casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Em quantos anos você prente parcelar? '))
prestacao = casa / (parcelas*12)

if prestacao > (salario*0.30):
    print('Desculpe, o financiamento não foi aprovado.')
else:
    print(f'O valor mensal do seu financiamento é: R$ {prestacao:.2f}.')