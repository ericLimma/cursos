from time import sleep

numeros = []

while True:

    digito = ''
    while not digito.isnumeric():
        digito = input('Digite um valor ou [=] para finalizar: ')
        if digito == '=':
            break

    if digito == '=':
        print('Finalizando...')
        sleep(1)
        break

    numeros.append(digito)
    numeros.sort(reverse=True)

print(f'Foram digitados {len(numeros)} números.\n'
      f'Números ordenados: {numeros}')

if '5' in numeros:
    print(f'O número 5 foi digitado {numeros.count("5")} vezes.')
else:
    print('O número 5 não foi digitado.')
