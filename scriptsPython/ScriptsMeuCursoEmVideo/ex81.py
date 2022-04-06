#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.
valores = list()
contagem = 0
cinco = 0
while True:
    val = int(input('Digite um valor:'))
    contagem += 1
    valores.append(val)
    if val == 5:
        cinco += 1
    cont = str(input('Você quer continuar adicionando numeros? (S/N): \n')).upper()[0]
    if cont != 'S':
        break
valores.sort()
print(f'A sua lista de valores foi: {valores}')
print(f'O numero de valores digitados foi {contagem}')
valores.reverse()
print(f'A sua lista de valores de forma descrescente foi: {valores}')
if cinco > 0:
    print(f'O valor 5 está presente na lista e foi digitado {cinco} vezes')
else:
    print(f'O valor 5 NÃO está presente na lista')
