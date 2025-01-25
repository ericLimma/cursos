"""Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag). Mostrar também a quantidade de números"""
from time import sleep
soma = count = 0

while True:

    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    soma += num
    count += 1

print(f'Analisando...')
sleep(1)
print(f'A soma dos {count} números que você digitou é: {soma}')
