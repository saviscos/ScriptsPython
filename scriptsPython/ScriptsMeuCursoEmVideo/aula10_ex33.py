#Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
#n1 = float(input('Digite o primeiro numero:'))
#n2 = float(input('Digite o segundo numero:'))
#n3 = float(input('Digite o terceiro numero:'))
#lista = [n1,n2,n3]
#m1 = sorted(lista)
#print(m1)
#print('O numero menor é o {}'.format(m1[0]))
#print('O numero maior é o {}'.format(m1[2]))

#outra forma de resolver
a = float(input('Digite o primeiro numero:'))
b = float(input('Digite o segundo numero:'))
c = float(input('Digite o terceiro numero:'))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(' o maior valor é {}.'.format(maior))
