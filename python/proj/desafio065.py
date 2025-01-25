"""Crie um programa que leia vários números inteiros pelo teclado. No final mostre a média entre todos os valores e
qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar
valores em vez disso, usar tecla = """

from time import sleep

continuar = 'S'
while continuar not in 'Nn':
    num = ''
    soma = count = 0
    lista = []
    while num != '=':
        num = input('Digite um número ou [=] para a análise: ')
        if num != '=':
            num = int(num)
            soma += num
            lista.append(num)
            count += 1

    menor = sorted(lista)[0]
    maior = sorted(lista)[-1]

    print('Analisando...')
    sleep(1)

    print(f'Análise dos {count} números que você digitou:\n'
          f'Maior: {maior}\n'
          f'Menor: {menor}\n'
          f'soma: {soma}\n'
          f'média: {soma/count:.2f}')
    continuar = input('Você deseja continuar? [s/n] ').strip().upper()
print('Até mais!')
