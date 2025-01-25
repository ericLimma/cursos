tempo = int(input('Qual a idade do seu carro? '))

"""condição composta"""

if tempo <= 3:
    print('Carro novo')
else:
    print('Carro Velho')

"""Condição Simplificada"""
print('Carro novo' if tempo<=3 else 'Carro Velho')