#Exercício Python 061: Refaça o DESAFIO 051,
#lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
cont = 1
r = int(input('Digite a razão da PA:'))
a1 = int(input('Digite o primeiro termo da PA:'))
while cont != 10:
    an = a1 + (cont-1)*r
    cont = cont + 1
    print('Os termo da progressão são:{} '.format(an) if cont == 2 else 'e {} '.format(an), end='')


