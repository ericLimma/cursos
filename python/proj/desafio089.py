"""Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final,
mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar notas de cada aluno
individualmente.

** numero de matricula??"""
from time import sleep

lista = []
aluno = []

while True:
    aluno.append(input('Digite o nome: ').strip().capitalize())

    for c in range(1, 3):  # digitar nota, garante que nota seja válida sem quebrar programa
        while True:
            nota = input(f'Digite a {c}ª nota de {aluno[0]}: ')
            nota = nota.replace(',', '.')
            if nota.isnumeric():
                nota = float(nota)
                if 0 <= nota <= 10:
                    break
        aluno.append(nota)
    lista.append(aluno[:])
    aluno.clear()

    cont = " "
    while cont not in "SN":
        cont = input('Deseja continuar? [S/N] ').strip().upper()
    if cont == 'N':
        break
lista = sorted(lista)
#  boletim
print(f'{"-" * 40}\n'
      f'\33[32m{"Boletim Escolar":^40}\33[m\n'
      f'{"-" * 40}')
print(f'\33[32m{"Nº":<10}{"Nome":<20}{"Média":<5}\33[m')

for num, aluno in enumerate(lista):
    print(f'{num:<10}'
          f'{aluno[0]:<20}', end='')
    media = (aluno[1]+aluno[2])/2

    if media < 5:
        print(f'\33[31m{media:<5}\33[m')
    else:
        print(f'\33[32m{media:<5}\33[m')
    sleep(.5)

# consulta individual

while True:
    print(f'{"-" * 40}\n')

    while True:  # garante que a opção desejada seja um número, e que esteja na lista de alunos.
        consulta = input('Qual aluno deseja consultar? ([999] para encerrar) ')
        if consulta.isnumeric():
            consulta = int(consulta)
            if consulta < len(lista) or consulta == 999:
                break
            else:
                print(f'\33[31mAluno não matriculado, tente novamente...\33[m')
        else:
            print(f'\33[31mOpção inválida, tente novamente...\33[m')

    if consulta == 999:  # encerra consulta
        print(f'{"-" * 40}\n')
        break

    print(f'A notas de {lista[consulta][0]} são: {lista[consulta][1]} e {lista[consulta][2]}.')
