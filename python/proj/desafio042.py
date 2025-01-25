"""Refaça o desafio dos triângulos, acrescentando o recurso de mostrar que tipo de
triângulo será formado:
 - Equilátero: todos os lados iguais
 - Isósceles: dois lados iguais
 - Escaleno: todos os lados diferentes"""

retaA = float(input('Digite a primeira medida: '))
retaB = float(input('Digite a segunda medida: '))
retaC = float(input('Digite a terceira medida: '))

if (retaA + retaB > retaC) and (retaC + retaA > retaB) and (retaB + retaC > retaB):
    if retaA == retaB == retaC:
        print('É um triângulo Equilátero!')
    elif retaA != retaB != retaC != retaA:
        print('É um triângulo Escaleno!')
    else :
        print('É um triângulo Isósceles!')
else:
    print('Não é um triângulo!')