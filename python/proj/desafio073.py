times = ('Palmeiras', 'Flamengo', 'Corinthians', 'Internacional', 'Fluminense', 'Athletico-PR', 'Atlético-MG',
         'América-MG', 'Goiás', 'Santos', 'Bragantino', 'Fortaleza', 'Botafogo', 'São Paulo', 'Ceará', 'Cuiabá',
         'Coritiba', 'Avaí', 'Atlético-GO', 'Juventude')

print(f'Os cinco primeiros colocados são:\n{", ".join(times[0:5])}.\n\n'
      f'Os últimos quatro colocados são: \n{", ".join(times[-4:-1])}.\n\n'
      f'O Bragantino está na {times.index("Bragantino")+1}ª colocação.\n\n'
      f'Lista dos 20 times em ordem alfabética: \n{", ".join(sorted(times))}.')
