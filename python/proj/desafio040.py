"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma
mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média entre 7.0 ou superio: APROVADO"""

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) /2

if media < 5:
    print(f'\33[31mSua média é {media}. Infelizmente, você foi REPROVADO!')
elif 5 < media < 7 :
    print(f'\33[33m Atenção, sua média é {media}, você está de RECUPERAÇÂO!')
elif media > 7:
    print(f'\33[32m Sua média é {media}, você PASSOU!')