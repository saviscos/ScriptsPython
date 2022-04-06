#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Digite o valor da casa:'))
salario = float(input('Digite o valor do salario:'))
tempo = float(input('Digite o tempo de pagamento em anos:'))
meses = tempo*12
prestação = casa/meses
print('A prestação é {}'.format(prestação))
sal30 = (salario*30)/100
print('30% do salário do cliente é: {}'.format(sal30))
if sal30 > prestação:
    print('O emprestimo foi aprovado')
else:
    print('O emprestimo não foi aprovado')
