#Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
n = int(input('Digite um valor inteiro:'))
cont = 0
soma = n
while n != 999:
    cont = cont + 1
    n = int(input('Digite um valor inteiro:'))
    soma += n
print('Foram digitados {} numeros e a soma de todos os numeros é {}'.format(cont, soma-999))



