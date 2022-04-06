#Exercício Python 061: Refaça o DESAFIO 051,
#lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('SAVISCO P.A ULTRA MASTER SOFTWARE')
cont = 1
r = int(input('Digite a razão da PA:'))
a1 = int(input('Digite o primeiro termo da PA:'))
cont2 = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont != total:
        an = a1 + (cont-1)*r
        cont = cont + 1
        print('Os termo da progressão são:{} '.format(an) if cont == 2 else 'e {} '.format(an), end='')
    mais = int(input('Quantas termos você quer a mais?'))
print('A progressão foi finalizada com {} termos'.format(total))


#cont2 = 1
#termo = int(input('\n Quantos termos mais você quer?'))
#while cont2 != 10+termo:
#    if termo != 0:
#        an = a1 + (cont2-1)*r
#        cont2 = cont2 + 1
#        print('Os termo da progressão são:{} '.format(an) if cont == 2 else 'e {} '.format(an), end='')
#   else:
#       print('Obrigado por usar o SAVISCO P.A ULTRA MASTER SOFTWARE')
