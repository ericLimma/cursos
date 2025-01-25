palavras = ('abacate', 'acerola', 'manga', 'uva', 'jilo', 'caramelo', 'pudim', 'quindim', 'morango', 'pera', 'melancia',
            'abobora', 'goiaba', 'laranja', 'caju', 'banana', 'castanha')

for c in palavras:
    print(f'\n\33[mAs vogais de {c.capitalize()} são: ', end='')
    for n in c:
        n = n.upper()

        if n in 'AEIOU':
            print(f'\33[32m{n}', end=' ')
