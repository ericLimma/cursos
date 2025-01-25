from random import randint

num = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))
print(f'Os valores sorteados foram: {(num)}')


'''menor = maior = count = 0

for c in num: #### Solução 1
    count += 1

    if count == 1 or c < menor:
        menor = c
        
    if count == 1 or c > maior:
        maior = c
'''

print(f'\nO maior valor sorteado foi: {max(num)}\n'
      f'O menor valor sorteado foi: {min(num)}')
