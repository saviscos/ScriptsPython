#Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
gasto = mil = 0
barato = float("inf")
while True:
    nom = str(input('Qual o produto?'))
    preco = int(input('Qual seu preço?'))
    gasto += preco
    if preco > 1000:
        mil += 1
    if preco < barato:
        barato = preco
        a = nom
    cont = ''
    while cont not in 'SN':
        cont = str(input('Você quer continuar?[S/N]')).strip().upper().split()[0]
    if cont == 'N':
        break
    print('---'*15)
print(f'O produto mais barato foi o {a} que custou {barato} reais')
print(f'A quantidade de produtos que custam mais de mil reais é de {mil}')
print(f'O valor da sua compra foi de {gasto} reais')
