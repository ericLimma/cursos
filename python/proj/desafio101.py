"""Desafio 101 - Crie um programa que tenha função chamada voto() que vai receber como parâmetro o ano de nascimento
de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL, ou OBRIGATÓRIO nas
eleições. """
from datetime import date


def voto(ano):

    """recebe o ano de nascimento e calcula se usuário já pode ou não votar."""
    idade = date.today().year - ano

    if 16 <= idade < 18 or idade >= 70:
        return 'Opcional'

    if 18 <= idade < 70:
        return 'Obrigatório'

    if idade < 16:
        return 'Negado'


ano = int(input('Ano de nascimento: '))

print(voto(ano))
