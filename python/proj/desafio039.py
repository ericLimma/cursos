"""Faça um programa que leeia o ano de nascimento ded um jovem e informe, de acordo com sua idade:
- se ele ainda vai se alistar ao serviço militar.
- se é a hora de se alistar.
- se já passou do tempo do alistamento.

seu programa também deverá mostrar o tempo que falta ou que passou do prazo"""
from datetime import date
sexo = str(input('''Qual o seu sexo?
[F] Feminino
[M] Masculino
Digite uma oção: ''')).strip().upper()

if sexo == 'F':
    print('Mulheres não precisam se alistar.')
elif sexo == 'M':
    nascimento = int(input('Digite o ano de seu nascimento: '))
    anoAtual = date.today().year
    idade = anoAtual - nascimento
    faltando = idade - 18

    if idade < 18 :
        print(f'Ainda não chegou sua vez, faltam {faltando *-1} anos para você se alistar!'
              f'\nVocê deve se alistar em {anoAtual + (faltando *-1)}')
    elif idade == 18:
        print(f'Já está na sua vez, hora de se alistar!!')
    else:
        print(f'Já passou da hora, você está {faltando} anos atrasado! \n'
              f'Você devia ter se alistado em {anoAtual - faltando}')
else:
    print('Digite uma opção válida')