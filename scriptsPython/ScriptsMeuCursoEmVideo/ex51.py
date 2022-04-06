#Exercício Python 051: Desenvolva um programa que leia
#o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
cont = 0
r = int(input('Digite a razão da PA:'))
a1 = int(input('Digite o primeiro termo da PA:'))
for c in range(2,12):
    an = a1 + (c-1)*r
    cont = cont + 1
    print('O termo numero {} da progressão é: {}'.format(cont,an))

#end=('→')
