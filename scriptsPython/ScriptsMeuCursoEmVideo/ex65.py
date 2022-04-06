#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
n = int(input('Digite um valor inteiro:'))
a = 'S'
cont = 1
soma = n
list = [n]
while a == 'S':
    cont = cont + 1
    n = int(input('Digite um valor inteiro:'))
    soma += n

    a = str(input('Você quer continuar? [S/N]')).upper().strip()[0]
    list.append(n)
    print('A média foi de: {}, o MENOR valor foi {} e o MAIOR valor foi {}'.format(soma / cont, min(list), max(list)))
print('Obrigado')
