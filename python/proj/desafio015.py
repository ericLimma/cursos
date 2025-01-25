dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram rodados? '))
valor = (dias * 60) + (km * 0.15)

print(f'O total a pagar é de R$ {valor:.2f}')
