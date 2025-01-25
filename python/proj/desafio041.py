"""A confederação nacional de natação precisa de um programa que leia o ano de
nascimento de um atleta e mostre sua categoria, de acordo com a idade:
 - até 9 anos: MIRIM
 - até 14 anos: INFANTIL
 - até 19 anos: JUNIOR
 - até 20 anos: SÊNIOR
 - acima: MASTER"""
from datetime import date
ano = int(input('Digite o ano de seu nascimento: '))
idade = date.today().year - ano

if idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <=19:
    print('Categoria JÚNIOR')
elif idade <=20:
    print('Categoria SÊNIOR')
elif idade > 20:
    print('Categoria MASTER')