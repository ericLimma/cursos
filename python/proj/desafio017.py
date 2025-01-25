"""faça um programa que leia o comprimento do cateto oposto e do cateto adjacente deed um
triangulo retangulo, calule e mostre o comprimento da hipotenusa
h²=ca²+co²"""

import math

co = float(input('Digite a medida do primeiro cateto: '))
ca = float(input('Digite a medida do segundo cateto: '))
'''poderia ser: h = (co ** 2 + ca ** 2) ** (1/2)'''
print(f'O valor da hipotenusa é: {math.hypot(co, ca):.2f}')
