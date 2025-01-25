"""Faça um programa que leia o sexo de uma pessoa, mas só aceite 'M' ou 'F'. Caso esteja errado. peça a digitação
novamente até ter um correto. """
sexo = ''
sexoEscolhido = ''
while 'F' != sexo != 'M':
    sexo = str(input('Qual seu sexo? [F/M] ')).upper().strip()
    print(sexo)
    if sexo == 'M':
        sexoEscolhido = 'Masculino.'
    elif sexo == 'F':
        sexoEscolhido = 'Feminino.'
print(f'Certo, seu sexo é {sexoEscolhido}')
