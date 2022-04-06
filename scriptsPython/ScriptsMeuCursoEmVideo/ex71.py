#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
#ced1 = ced10 = ced20 = ced50 = 0
#saque = int(input('Qual valor você gostaria de sacar: R$'))
#while True:
#    while saque - 50 >= 0:
#       ced50 += 1
#        saque = saque - 50
#   while saque - 20 >= 0:
#        ced20 += 1
#       saque = saque - 20
#   while saque - 10 >= 0:
#        ced10 += 1
#        saque = saque - 10
#    while saque - 1 >= 0:
#        ced1 += 1
#        saque = saque - 1
#    if saque == 0:
#        break
#print(f'''Total de {ced50:5} cédulas de R$50,00.
#total de {ced20:5} cédulas de R$20,00.
#total de {ced10:5} cédulas de R$10,00.
#total de {ced1:5} cédulas de R$1,00.''')

valor = int(input("informe o valor a ser sacado : "))
nota50 = valor // 50
valor %=  50
nota20 = valor // 20
valor %= 20
nota10 = valor // 10
valor %= 10
nota1 = valor // 1
print(f"notas de 50 = {nota50}")
print(f"notas de 20 = {nota20}")
print(f"notas de 10 = {nota10}")
print(f"notas de 1 = {nota1}")
