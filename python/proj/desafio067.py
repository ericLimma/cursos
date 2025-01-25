"""Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O
programa será interrompido quando o número solicitado for negativo."""


while True:
    print('-'*20)
    n = int(input('Digite um número: '))
    print('-'*20)

    if n <= 0:
        break

    c = 0
    while c <= 10:
        print(f'{n} x {c} = {n * c}')
        c += 1

print('Até logo!')
