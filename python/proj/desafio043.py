"""Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e
mostre seu status de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: PEso ideal
- 25 aaté 30: Sobrepeso
- 30 - 40: Obesidade
- Acima dee 40: Obesidade mórbida"""

peso = float(input('Digite seu peso em quilogramas: '))
altura = int (input('Digite sua altura em centímetros: '))

imc = peso / ((altura/100)**2)

if imc < 18.5 :
    print(f'IMC: {imc:.2f}, Abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print(f'IMC: {imc:.2f}, Peso ideal!')
elif imc >= 25 and imc < 30:
    print(f'IMC: {imc:.2f}, Sobrepeso')
elif imc >= 30 and imc < 40:
    print(f'IMC: {imc:.2f}, Obesidade!')
else:
    print (f'IMC: {imc:.2f}, Obesidade Mórbida!')
