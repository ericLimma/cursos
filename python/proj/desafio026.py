"""Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A".
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a última vez."""

frase = str(input('Digite uma frase: ')).strip().upper()
print(frase.count("A"))

if frase.count("A") >= 1:
    print(f'Nessa frase:\n'
          f'Aparecem {frase.count("A")} vezes a lera "A"\n'
          f'Aparece pela primeira vez na posição {frase.find("A") + 1}\n'
          f'e pela última vez na posição {frase.rfind("A") + 1}')
else:
    print('Sua frase não possui letra "A"')
