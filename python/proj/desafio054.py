"""Crie um programa que leia o ano de 7 pessoas. No final, mostre quantas pessoas ainda
não atingiram a maioridade e quantas já são mariores
considerar 21 anos como maior de idade"""

from datetime import date
ano = date.today().year
maiores = 0
menores = 0

for c in range (1, 8):
    nascimento = int(input("Digite o ano do nascimento: "))
    if ano - nascimento < 21:
        menores += 1
    elif ano - nascimento > 21:
        maiores += 1

print(f'A quantidade de maiores de idade é: {maiores}, \n'
      f'e a quantide de menores de idade é: {menores}!')
