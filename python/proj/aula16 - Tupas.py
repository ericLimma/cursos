lancheT1 = ('Hamburger', 'Suco', 'Pizza', 'Pudim')  # Tupla — considera cada palavra como um elemento distinto
lancheT2 = 'Hamburger', 'Suco', 'Pizza', 'Pudim'  # Tupla — considera cada palavra como um elemento distinto
lancheT3 = 'Hamburger, Suco, Pizza, Pudim'  # Tupla - considera cada carácter como um elemento

lancheL1 = ['Hamburger, Suco, Pizza, Pudim']  # Lista — considera tudo como um elemento só
lancheL2 = ['Hamburger', 'Suco', 'Pizza', 'Pudim']  # Lista — considera cada palavra como um elemento distinto

print(f'ex.1: {lancheT1[0]}\n'  # consigo acessar o elemento [i]
      f'ex.2: {lancheT1[0][0]}\n'  # consigo acessar o elemento [i], dentro elemento [i]
      f'ex.3: {lancheT1[0:]}\n'  # mostra do 0 até o último
      f'ex.4: {lancheT1[-1]}\n'  # índice negativo, mostra do último (-1), penúltimo (-2), em diante
      f'ex.5: {lancheT1[0:3]}\n'  # vai do 0 ao 2 (desconsidera o 3)
      f'ex.6: {sorted(lancheT1)}\n'  # exibe a tupa/lista em ordem crescente
      f'ex.7: {", ".join(lancheT1)}\n')  # exibe a tupa/lista sem aspas separado por virgula

a = (1, 3, 5)
b = (2, 4, 5)
c = a + b  # resultado: (1, 3, 5, 2, 4, 5), junta uma tupla na outra
c = b + a  # resultado: (2, 4, 5, 1, 3, 5), a ordem altera o resultado

print(f'\nex.8: {c.count(5)}\n'  # conta quantas vezes o 5 aparece na tupla/lista
      f'ex.9: {c.index(5)}\n')  # retorna a posição da primeira ocorrência do 5
