#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
# condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros
valor = float(input('Digite o valor do produto:'))
print('''O valor será pago como: 
[ 1 ] à vista dinheiro/cheque: 10% de desconto
[ 2 ] à vista no cartão: 5% de desconto
[ 3 ] em até 2x no cartão: preço formal
[ 4 ] 3x ou mais no cartão: 20% de juros
''')
pag = int(input('Digite uma opção:'))
if pag == 1:
    desc = (valor * 10) / 100
    valor = valor - desc
    print('O valor será de {}'.format(valor))
elif pag == 2:
    desc = (valor * 5) / 100
    valor = valor - desc
    print('O valor será de {}'.format(valor))
elif pag == 3:
    parcelas = valor/2
    print('O valor será de {}, com parcelas de {}'.format(valor,parcelas))
elif pag == 4:
    parcelas = int(input('Digite a quantidade de parcelas:'))
    if parcelas == 1:
        print('O valor será de uma parcela de {}'.format(valor))
    elif parcelas == 2:
        novovalor = valor/2
        print('O valor total é de {}, com {} parcelas de {}'.format(valor,parcelas,novovalor))
    elif parcelas >= 3:
        desc = (valor * 20) / 100
        valor = valor + desc
        novovalor = valor/parcelas
        print('O valor será de {}, com {} parcelas de {}'.format(valor,parcelas,novovalor))
    else:
        print('O valor de parcelas esta errado')
