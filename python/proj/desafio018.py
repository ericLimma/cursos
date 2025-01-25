"""faça um programa que leia um angulo qualquer e mostre na  tela o valor do seno,
cosseno e tangente desse angulo"""

from math import sin, cos, tan, radians

angulo = float(input('Digite o valor do ângulo: '))

print(f'Ângulo digitado:  {angulo}º\n'
      f'Seno do ângulo: {sin(radians(angulo)):.2f}\n'
      f'Cosseno do ângulo: {cos(radians(angulo)):.2f}\n'
      f'Tangente do ângulo:{tan(radians(angulo)):.2f}')

'''radians converte para radiano'''
