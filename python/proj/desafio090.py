"""Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final,
mostre o conteúdo da estrutura na tela
** pedir às duas notas"""

aluno = dict()
aluno['nome'] = input('Digite nome do aluno: ').capitalize(),
aluno['media'] = (int(input('Digite a primeira nota: ')) + int(input('Digite a segunda nota: ')))/2

if aluno["media"] >= 5:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'

print(f'\nAluno: {aluno["nome"]} \n'
      f'Média: {aluno["media"]} \n'
      f'Situação: {aluno["situacao"]}')
