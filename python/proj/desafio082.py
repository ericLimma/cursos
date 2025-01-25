numeros = []
pares = []
impares = []

while True:

    while True:
        digito = input('Digite um valor ou [=] para sair: ')
        if digito == '=' or digito.isnumeric():
            break

    if digito == '=':
        break

    numeros.append(int(digito))

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f'Os números pares são: {pares}\n'
      f'Os números ímpares são: {impares}')
