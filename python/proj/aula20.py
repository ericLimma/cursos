'''def teste(b):
    """Função para teste em aula."""
    a = 1
    a += 8
    b += 4
    c = 2
    print(f'Dentro')
    print(f'A vale: {a}')
    print(f'B vale: {b}')
    print(f'C vale: {c}')


a = 5
teste(a)
print('fora')
print(f'A vale: {a}')
print(f'B vale: {b}')
print(f'C vale: {c}')
'''  # escopo de variável


'''def soma(a=0, b=0, c=0):  # dessa forma, os parâmetros são opcionais.
    s = a + b + c
    return s  # retorna o valor de s para a quem está chamando a função


print(f'Somas: ')
print(soma(2, 5, 9))
print(soma(1, 2))
print(soma(4))

# ou

r1 = soma(1, 5, 6)
r2 = soma(1, 2, 6)
r3 = soma(1, 3, 6)

print(f'Os resultados foram {r1}, {r2}, {r3}')'''  # return
