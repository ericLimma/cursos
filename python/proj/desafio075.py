n = (int(input('Digite um número: ')),
     int(input('Digite um número: ')),
     int(input('Digite um número: ')),
     int(input('Digite um número: ')))

if n.count(9) == 1:
    print(f'O número 9 foi digitado {n.count(9)} vez.')
elif n.count(9) > 1:
    print(f'O número 9 foi digitado {n.count(9)} vezes.')
elif n.count(9) == 0:
    print(f'O número 9 não foi digitado')

if 3 in n:
    print(f'O 3 foi digitado na {n.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado.')

print(f'O números pares digitados foram: ', end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')