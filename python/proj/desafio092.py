"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um
dicionário se por acaso a ctps for diferente de zero o dicionário receberá também o ano dde contratação e o salário.
calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
***35 anos de carteira"""
from datetime import date

ano = date.today().year
p = dict(nome=input('Digite o nome: ').capitalize(),
         nascimento=int(input('Digite o ano de nascimento: ')),
         cpts=int(input('Digite o número da carteira de trabalho: ')))

p['idade'] = ano - p['nascimento']

if p['cpts'] > 0:
    p['contratacao'] = int(input('Qual o ano de sua contratação? '))
    p['salario'] = int(input('Qual o salário? '))
    p['aposentadoria'] = (p['contratacao'] + 35) - p['nascimento']

for k, v in p.items():
    print(f'\n{k.capitalize()} = {v}')
