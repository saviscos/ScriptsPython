#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores 'M' ou 'F'.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.
#s = 'X'
#while s == 'X':
#    s = str(input('Digite o sexo da pessoa [M/F]:')).upper()
#   if s == 'M' or s == 'F':
#        print('Você digitou {}'.format(s))
#        s = 'Y'
#    else:
#        s = 'X'
#        print('Tente novamente')
#print('Fim')

#s = ''
#while s != 'M' and s != 'F':
#    s = str(input('Digite um sexo: [M/F] ').upper().strip())
#   if s != 'F' and s != 'M':
#       print('Favor digitar uma opção de sexo válida (M/F).')
#    else:
#        print('Você digitou {}.'.format(s))
#print('Acabou')

sexo = str(input('Digite um sexo [M/F]:')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Digite um sexo [M/F]:')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

