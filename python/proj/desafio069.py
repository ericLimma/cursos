"""Crie um programa que leia a idade e sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final, mostre?

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
c) quantas mulheres tem menos de 20 anos.

 Enquanto não colocar a opção correta, deve se perguntar novamente"""

from time import sleep

homens = mulheres = pessoas = 0

while True:
    sexo = ' '  # precisa ter um espaço para funcionar

    while sexo not in 'FM':
        sexo = str(input('Qual o sexo? [f/m] ')).upper().strip()[0]
    idade = int(input('Digite a idade: '))

    if idade >= 18:
        pessoas += 1

    if sexo == 'M':
        homens += 1
    elif sexo == 'F':
        if idade <= 20:
            mulheres += 1
            print("HERE")

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [s/n] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('Analisando...')
sleep(1)
print(f'Resultado:\n'
      f'Pessoas Maiores de 18 anos: {pessoas}\n'
      f'Homens cadastrados: {homens}\n'
      f'Mulheres com menos de 20 anos: {mulheres}\n')

print('Finalizando...\n'
      'Até mais!!')
