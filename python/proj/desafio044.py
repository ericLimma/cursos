"""Elabore um prgrama que calcule o valor a ser pago por um produto, considerando o seu preço normal
e condição de pagamento:
 - à vista dinheiro/pix: 10% de desconto
 - à vista no cartão: 5% de desconto
 - em até 2x no cartão: preço normal
 - 3x ou mais no cartão: 20% de juros"""

valor = float(input('Qual o valor do produto? '))
formaPag = int(input('''\nQual a forma de pagamento?
[1] Dinheiro
[2] Cartão
Digite uma opção: '''))

if formaPag == 1:
    print(f'Valor total com desconto: R$ {(valor - (valor * 0.1)):.2f}')
elif formaPag ==2:
    parcelas = int(input('\nEm quantas vezes? '))
    if parcelas == 1:
        print(f'Valor total com desconto: R$ {(valor - (valor * 0.05)):.2f}')
    elif parcelas == 2:
        print(f'Valor da parcela: R$ {valor/2:.2f}\n'
              f'Valor total: R$ {valor:.2f}')
    elif parcelas >= 3 :
        valorComJuros = valor + (valor * 0.2)
        print(f'Valor da parcela : R$ {valorComJuros/parcelas:.2f}\n'
              f'Valor total com juros: R$ {valorComJuros:.2f}')
    else:
        print('Digite uma forma de pagameno válida')
else:
    print('Digite uma forma de pagamento válida!')