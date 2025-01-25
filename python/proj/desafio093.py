"""Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final , tudo isso será
guardado em um dicionário, incluindo o total de gols feitos durante o campeonato. """

j = dict(nome=str(input('Digite o nome: ')).capitalize(),
         gols=[],
         total=0)

nPartidas = int(input('Quantas partidas ele jogou? '))

for c in range(1, nPartidas + 1):
    g = int(input(f'Quantos gols ele marcou na {c}ª partida? '))
    j['gols'].append(g)
j['total'] = sum(j["gols"])
print(j)

print('-='*20)

for k, v in j.items():
    print(f'O campo {k} tem o valor {v}.')

print('-='*20)

print(f'O jogador {j["nome"]} jogou {nPartidas} partidas.')

for i, p in enumerate(j['gols']):
    print(f'    - Na {i+1}ª partida, ele marcou {p} gols.')

print(f'Foi um total de {j["total"]} gols.')
