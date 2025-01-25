numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:

    valido = False
    num = 0
    while True:
        num = int(input('Digite um número inteiro: '))
        if 0 <= num <= 20:
            break

    print(f'Você digitou: {str(numeros[num]).capitalize()}\n')
