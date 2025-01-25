lfixa = []

count = 1
while True:
    ltemp = []
    print(f'Cadastre a {count}ª pessoa...')
    ltemp.append(str(input('Nome: ')))
    ltemp.append(int(input('Idade: ')))
    lfixa.append(ltemp[:])
    count += 1
    sair = str(input('Deseja continuar? [s/n]')).strip().upper()[0]

    if sair == 'N':
        break
print(lfixa)