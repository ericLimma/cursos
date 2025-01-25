"""Desenvolva um programa que leia o primeiro termo e a razão de um Progressão
aritmética no final, mostre os primeiros termos dessa progressão."""

print('='*40,'\n10 termos de uma progressão aritimética\n','='*40)

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro +(10 - 1) * razao
for c in range (primeiro,decimo, razao):
    print(f'{c}',end= ' ')