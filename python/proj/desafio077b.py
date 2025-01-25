palavras = ['abacate', 'ácerola', 'manga', 'uva', 'jiló', 'caramelo', 'pudim', 'quindim', 'morango', 'pera', 'melancia',
            'abobora', 'goiaba', 'laranja', 'caju', 'banana', 'castanha']

for c in palavras:
    print(f'\33[mAs vogais de {c.capitalize()} são: ', end='')

    for n in c:
        n = n.upper()

        if n in 'AEIOU':
            print(f'\33[1:32m{n}', end=' ')
