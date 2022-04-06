#Exercício Python 050: Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
#s = 0
#for c in range(0,6):
#    n = float(input('Digite um numero inteiro:'))
#    if n%2 == 0:
#        s = n+s
#print('A somatoria dos numeros pares será: {}'.format(s))

s = 0
cont = 0
print('Digite seis números inteiros: ')
for c in range (0, 6):
    num = int(input(''))
    if num % 2 == 0:
        s += num
        cont += 1
print('A soma dos {} valores pares digitados é {}'.format(cont, s))



