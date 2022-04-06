#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
cont = 0
num = tuple()
nove = 0
tres = ''
pares = tuple()
while cont != 4:
    numero = tuple(input('Insira um numero:'))
    if numero[0] == '9':
        nove = nove + 1
    num = num + numero
    cont = cont + 1
    if numero[0] == '3':
        tres = cont
    par = numero[0]
    if par%2 == 0:
        par == pares
print('Os valores digitados foram:')
print(num)
print('Quantas vezes o nove foi digitado:')
print(nove)
print('Em que posição o 3 foi digitado na posição:')
print(f'{tres}º')
print('Os valores pares são:')
print(f'{par}')
