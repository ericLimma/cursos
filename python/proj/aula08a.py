# import math -- importa toda a lib
from math import sqrt, floor

# importa apenas as funções sqrt e floor da lib math,
# nesse caso não usamos mais o math.função()


num = int(input('Digite um número: '))
raiz = sqrt(num)

print(f'A raiz de {num} é igual a {raiz:.2f}')
