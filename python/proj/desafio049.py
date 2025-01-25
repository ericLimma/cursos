"""Faça uma tabuada de um número que o usuário escolher, só que agora ultilizando um
laço for"""

num = int(input('Digite um número: '))

for c in range (1, 11):
    print(f'\033[32m{num} x {c:2} = {num*c}')