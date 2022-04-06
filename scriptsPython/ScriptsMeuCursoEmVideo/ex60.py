#Faça um programa que leia um número qualquer e mostre o seu fatorial
#contador = 1
#numero = int(input('Digite um numero para fatorar: '))
#while numero >= 1:
#   contador *= numero
#    numero = numero - 1
#print(contador)

#-----------2----------
#from math import factorial
#n = int(input('Digite um numero'))
#print(factorial(n))

#-----3------
#n = int(input('Digite um numero pra fatorar:'))
#c = n
#f =  1
#while c > 0:
#    print('{}'.format(c), end='')
#    print('x' if c > 1 else ' = ', end='')
#    f = f * c
#    c -= 1
#print('{}'.format(f))

#------4
print('Leia aqui seu número fatorial!')
fat = int(input('Digite o número que desejas fatorar: '))
n = 0
prod = 1
print('{}!'.format(fat), end = '')
if fat == 0 or fat == 1:
    print(' = 1')
if fat != 0:
    while fat != 1:
        print(' x {}'.format(fat), end = '')
        prod *= fat
        fat = fat - 1
        if fat == 1:
            print(' = {}'.format(prod))