produtos = ('Caderno', 25,
            'Lápis', 2,
            'Caneta', 2.99,
            'Calculadora', 52.99,
            'Notebook', 1499,
            "Borracha", 3.99,
            'Lapiseira', 9.9,
            'Chaveiro', 7.99,
            'Sulfites', 49.90,
            'Cadeira', 6000,
            'Cartolina', 2.5,
            'Mouse', 59.9)
print(f'{"-" * 52:<52}\n{"Papelaria Waldemar":^52}\n{"-" * 52:<52}\n')
n = 0
for c in produtos:
    caracteres = 40 - len(str(produtos[n]))
    if n % 2 == 0:
        print(f'{c:<}{"." * caracteres}', end='')
    else:
        print(f'R$ {c:>7.2f}')
    n += 1
