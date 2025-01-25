"""Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada Km acima do limite"""

vel = int(input('Qual a velocidade? '))

if vel >= 80:
    print('MULTADO! Você ultrapassou o limite de velocidade de 80 km/h \n'
          f'Sua multa é de R$ {(vel - 80)*7 :.2f}!')
