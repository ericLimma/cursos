lista = []
maior = menor = 0
posicaoMaior = []
posicaoMenor = []
for c in range(1, 6):
    num = ' '
    while not num.isnumeric():
        num = input(f'Digite {c}º valor: ')
    lista.append(num)
    if c == 1 or num < menor:
        menor = num
    if c == 1 or num > maior:
        maior = num
for indice, item in enumerate(lista):
    if item == menor:
        posicaoMenor.append(indice)
    if item == maior:
        posicaoMaior.append(indice)
print(f'Maior: {maior}, índice: {posicaoMaior}\n'
      f'Menor: {menor}, índice: {posicaoMenor}\n'
      f'Lista: {" - ".join(lista)}')
