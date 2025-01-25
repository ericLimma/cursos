"""Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura WHILE. """

print(f'{"-"*30:<}\n{"Os 10 primeiros termos da PA":^30}\n{"-"*30:<}')

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
decimo = primeiro + (10 - 1) * razao
c = primeiro

while c < decimo:
    print(c, end=' ')
    c += razao
