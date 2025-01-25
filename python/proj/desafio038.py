"""Escreva um programa que leia dois númneros inteiros e compare-os, mostrando na tela
uma mensagem:

-O primeiro valor é maior
- O segundo valor pe maior
- não existe valor maior, os dois são iguais"""

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print('O primeiro número é maior')
elif num2 > num1:
    print('O segundo número é maior')
else:
    print('Não existe número maior, os dois são iguais')