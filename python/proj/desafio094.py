"""Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:

a) Quantas pessoas foram cadastradas
b) A média de idade do grupo
c) Uma lista com todas as mulheres.
d) uma lista com todas as pessoas com idade acima da média"""

from datetime import date
ano = date.today().year
cadastro = dict()
mulheres = []
# matricula = sexo (m/f), ano (22), Cpf(4 últimos)

while True:
    # recebe os dados
    t = {}
    t['nome'] = str(input('Nome: ')).capitalize()
    t['idade'] = int(input('Idade: '))
    t['cpf'] = str(input('CPF: '))
    sexo = ' '

    # cria um número de matrícula com base nas informações
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: '))[0].upper()
    t['sexo'] = sexo
    matricula = sexo + "-" + str(ano) + '-' + t['cpf'][-4:]
    cadastro[matricula] = t

    # condição de saída
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: '))[0].upper()
    if continuar == 'N':
        break

'''exibi oss resultados da pesquisa'''

soma = 0

# m = matricula, d = dados
for matricula, dados in cadastro.items():
    soma += dados['idade']
    if dados['sexo'] == 'F':
        mulheres.append(dados['nome'])

media = soma / (len(cadastro))

print(f'Pessoas cadastradas: {len(cadastro)} pessoa(s).')
print(f'Média de idade do grupo: {media:.2f} anos.')

# lista com as mulheres
print(f'Lista de mulheres cadastradas: ')
for mulher in mulheres:
    print(f'    - {mulher}')
print('Pessoas mais velhas que a média de idade: ')
for matricula, dados in cadastro.items():
    if dados['idade'] > media:
        print(f'    - {dados["nome"]}')
