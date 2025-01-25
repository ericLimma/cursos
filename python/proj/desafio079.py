from time import sleep

numeros = []

while True:

    digito = ''
    while not digito.isnumeric():
        digito = input('Digite um valor ou "=" para finalizar: ')
        if digito == '=':
            break
    if digito == '=':
        break
    if digito not in numeros:
        numeros.append(digito)
        print('Número adicionado...')
    else:
        print('Número ja existe!')

print('Finalizando...')
sleep(1)
print(f'Numeros Digitados: {" - ".join(numeros)}')
