# operadores
# + Soma
# - subtração
# * multiplicação
# / Divisão
# // Divisão Inteira
# % resto da divisão
# ** potenciação -- pow(4,3) = 4**3
# == igual a
# **(1/2) raiz quadrada


## no phyton usamos apenas parenteses na aritmética


# variações do print
nome = input('Qual seu nome?')
print('Prazer em te conhecer {}!'.format(nome))  # escreve o nome na mensagem
print('Prazer em te conhecer {:20}!'.format(nome))  # escreve o nome em 20 caracteres
print('Prazer em te conhecer {:>20}!'.format(nome))  # escreve o nome em 20 caracteres alinhado a direita
print('Prazer em te conhecer {:<20}!'.format(nome))  # escreve centralizado a esquerda
print('Prazer em te conhecer {:^20}!'.format(nome))  # escreve o nome centralizado
print('Prazer em te conhecer {:=^20}!'.format(nome))  # escreve o nome com o símbolo em volta

print('Número flutuante {:.3}'.format((10 / 3)))  # define o numero de casas decimais após o ponto
#quebra de linha
print('Exemplo de quebra de linha \nestou em outra linha')
print('Não quebrará linha', end=' ')
print('Continuo na mesma linha')