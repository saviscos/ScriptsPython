#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
#n = int(input('Digite o numero que queres analisar:'))
#for c in range(1,n):
#    if n%2 != 0 and n%1 == 0 and n%n == 0 :
#        print('O numero é primo')
#    else:
#        print('O numero não é primo')

num = int(input('Digite um número para verificar se ele é primo: '))
cont = 0
for c in range (1, num+1):
    if num%c == 0:
        cont += 1
if cont == 2:
    print('{} é um número primo!'.format(num))
else:
    print('{} Não é um número primo!'.format(num))
