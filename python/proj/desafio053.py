"""Crie um programa que leia uma frase qualquer e diga se ela é palíndromo,
desconsiderando os espaços
replace " ", "" """

frase = str(input('Digite uma frase: '))
fraseTrat = frase.replace(' ', '').lower()
fraseInv = ''.join(list(reversed(fraseTrat)))

if fraseTrat == fraseInv:
  print(f'A frase "{frase}" é um palíndromo.')
else:
    print(f'A frase "{frase}" não é um palíndromo.')
