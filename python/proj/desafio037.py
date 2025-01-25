"""Escreva um programa que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão:

- 1 para o binário
- 2 para octal
- 3 para hexadecimal"""

num = int(input('Digite um número: '))
opcao = int(input('''Escolha uma das opções para conversão:
[1] para binário, 
[2] para octal
[3] para hexadecimal
Digite sua opçao: '''))

if opcao == 1:
    print(f'O número {num} em binário é: {bin(num)[2:]}')  # [2:] Fatia a string
elif opcao == 2:
    print(f'O número {num} em octal é: {oct(num)[2:]}')
elif opcao == 3:
    print(f'O número {num} em hexadecimal é: {hex(num)[2:]}')
else:
    print('Digite uma opção válida!')