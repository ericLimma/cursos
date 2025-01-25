"""Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos"""

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
c = primeiro
escolha = 10
termos = ''
contador = 0
while escolha > 0:
    if escolha > 0:
        termos = c + escolha * razao

    while c < termos:
        print(c, end=' ')
        c += razao
    contador += escolha
    escolha = int(input('\nQuer ver mais quantos termos? '))

print(f'Finalizado com {contador} termos mostrados. \n \nAté mais!')
