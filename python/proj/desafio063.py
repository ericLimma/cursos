"""Escreva um programa que leia um número n inteiro qualquer e mostre a tela os n primeiros elementos de uma
sequência de fibonacci. ex.: 0 - 1 - 1 - 2 - 3 - 5 - 8 """

sair = 'N'
while sair not in 'Ss':

    n = int(input('Digite um número para começarmos: '))
    count = 3
    t1 = 0
    t2 = 1

    print(f'Sequência de Fibonacci: \n'
          f'{t1} - {t2} - ', end='')

    while count <= n:
        t3 = t1 + t2
        print(f'{t3}', end='')
        print('', end='' if count > n-1 else ' - ')
        t1 = t2
        t2 = t3
        count += 1
    sair = str(input('\nDeseja sair? [s/n] '))

print('Até a próxima!')
