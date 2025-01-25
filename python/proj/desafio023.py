"""Faça um programa que leia um número de 0 a 999 e mostre na tela cada um dos digitos
separados.
ex.: > Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1

tentar fazer matematicamente e como string"""

s = str(input('Digite um número de 0 a 9999: '))
num = '000' + s
print(f' Unidade: {num[-1]}\n'
      f' Dezena: {num[-2]}\n'
      f' Centena: {num[-3]}\n'
      f' Milhar: {num[-4]}\n')
