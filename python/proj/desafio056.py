"""Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas.
no final mostre:
 - A média de idade do grupo
 - Qual é o nome do homem mais velho.
 - Quantas mulheres tem menos de 20 anos."""

pessoas = int(input('Quantas pessoas participarão dessa pesquisa? '))
mulheresMenores = 0
idadeMaisVelho = 0
homem = 0
mulher = 0
media = 0

for c in range (1, pessoas+1):
    print('\n', '-'*5, c, 'º Pessoa', '-'*5 )
    nome = str(input('Nome: ')).strip().capitalize()
    sexo = str(input('Sexo [F/M]: ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('ERRO! Sexo inválido, recomece a pesquisa!')

    idade = int(input(f'{nome}, digite sua idade: '))

    if sexo == 'M':
        if idade > idadeMaisVelho:
            homemMaisVelho = nome
            idadeMaisVelho = idade
        homem +=1
    elif sexo == 'F':
        if idade < 20:
            mulheresMenores +=1
        mulher +=1

    media += idade

if homem >=1 :
    print(f'O homem mais velho é o {homemMaisVelho} e sua idade é {idadeMaisVelho} anos.')
else:
    print(f'Nenhum homem respondeu a pesquisa.')
if mulher >= 1:
    if mulheresMenores >=1:
        print(f'{mulheresMenores} mulher(es) tem menos de 20 anos.')
    else:
        print(f'Nenhuma mulher é menor de idade.')
else:
    print(f'Nenhuma mulher respondeu a pesquisa.')

print (f'A média de idade é: {media/2}.')
