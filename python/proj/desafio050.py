"""Desenvolva um programa que leia 6 numeros inteiros e mostre a soma apenas daqueles
que forem pares. se o valor digitado for ímpar, desconsidere-o"""
soma = 0

for c in range (1,7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
print(soma)