#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão
#conter apenas os valores pares e os valores ímpares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas geradas.
valores = list()
pares = list()
impares = list()
contagem = 0
while True:
    val = int(input('Digite um valor:'))
    contagem += 1
    valores.append(val)
    if val % 2 == 0:
        pares.append(val)
    else:
        impares.append(val)
    cont = str(input('Você quer continuar adicionando numeros? (S/N): \n')).upper()[0]
    if cont != 'S':
        break
valores.sort()
pares.sort()
impares.sort()
print(f'A sua lista de valores foi: {valores}')
print(f'A sua lista de valores foi: {pares}')
print(f'A sua lista de valores foi: {impares}')
