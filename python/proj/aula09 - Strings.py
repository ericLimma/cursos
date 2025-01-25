"""Manipulando texto"""

frase = 'Curso em video Python'
frase2 ='  Aprenda Python  '
frase3 = ['frase', 'separada']
"""Análise de Strings"""
print(f'\n\nFrase completa: {frase}')
print(f'Vai do 9 ao 21, pulando de 2 em 2: {frase[9:21:2]}')
print(f'começa na posição 0, indo até a posição: {frase[:5]}')
print(f'Começa na posição 15 e vai até o final da string: {frase[15:]}')
print(f'Começa na posição 9 e vai até a o final, de 3 em 3: {frase[9::3]}')
print(f'Mostra o comprimento da string/lista: {len(frase)}')
print(f'Contabiliza todas as ocorrencias dde um caracter na string: {frase.count("o")}')
print(f'Contabiliza todas as ocorrencias de um caracter em uma fatia da string:'f''
      f' {frase.count("o", 0, 13)}')
print(f'vai me dizer a posição que ocorre um caracter ou sequencia de caracter em uma '
      f'string: {frase.find("deo")}\n\n')  # caso não exista, retorna o valor -1

"""Tratando strings"""

print('Vai substitui o o primeiro argumento pelo segundo argumento: {}'.format(
    frase.replace('Python', 'Android')))
print(f'Deixa string em maiúscula: {frase.upper()}')
print(f'Deixa string em minúscula: {frase.lower()}')
print(f'Deixa string em minúscula porém primeira letra maiúscula: {frase.capitalize()}')
print(f'Analisa quantas palavras tem na frase e deixa primeiras letras maiúsculas:'
      f' {frase.title()}')
print(f'Remove espaços inúteis(da direita e esquerda): {frase2.strip()}')
print(f'Remove espaços inúteis (da direita): {frase2.rstrip()}')
print(f'Remove espaços inúteis(da esquerda): {frase2.lstrip()}\n\n')

"""Divisão de strings"""

print(f'Vai dividir frase, considerando onde tem espaços na frase: {frase.split()}')

frase.split()
print(f'Vai juntar frases separadas, em uma frase, separando pelo caracter desejado: '
      f'{frase3, " ".join(frase3)}')
