numeros = []

for c in range(0, 5):

    n = int(input('Digite um número: '))

    if c == 0:
        numeros.append(n)
        print('Primeiro número adicionado')
    elif n > numeros[-1]:
        numeros.append(n)
        print('Adicionado na última posição!')
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f'Número adicionado na posição {pos} da lista')
                break
            pos +=1
print(numeros)
