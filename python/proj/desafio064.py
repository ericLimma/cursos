"""Crie um programa que leia vários números inteiros pelo teclado. O programa só vai para quando o usuário digitar o
valor 999, que é a condição de parada No final, mostre quantos números foram digitados e qual foi a soma entre eles,
desconsiderando a flag """

c = 0
soma = 0
contador = 0

while c != 999:
    c = int(input('Digite um número: '))
    if c != 999:
        soma += c
        contador += 1
print(f'Você digitou {contador} números, e a soma deles é: {soma}')
