#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
dados = list()
pessoas = list()
pesos = list()
pesosSort = list()
contpess = 0
contmenpes = 0
contmaipes = 0
while True:
    dados.append(str(input('Digite o nome:')))
    contpess += 1
    dados.append(float(input('Digite o peso:')))
    pessoas.append(dados[:])
    pesos.append(dados[1])
    nomes.append(dados[0])
    dados.clear()
    continuar = str(input('Você quer continuar digitando nomes? [S/N]').upper()[0])
    if continuar == 'N':
        break
print(f'Foram cadastradas {contpess} pessoas')
pesosSort = sorted(pesos)
menorpeso = pesosSort[0]
maiorpeso = pesosSort[contpess-1]
for c in pesos:
    contmenpes += 1
    if c == menorpeso:
        break
print(f'A pessoa com menor peso foi {pessoas[contmenpes-1][0]} pesando {menorpeso}')
for c in pesos:
    contmaipes += 1
    if c == maiorpeso:
        break
print(f'A pessoa com maior peso foi {pessoas[contmaipes-1][0]} pesando {maiorpeso}')
