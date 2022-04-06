#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um numero inteiro:'))
opção = int(input('Digite sua conversão. \n 1 para binário \n 2 para octal \n 3 para hexadecimal:'))
if opção == 1:
    print('Seu numero em binário é {}'.format(bin(num)))
elif opção == 2:
    print('Seu numero em octal é {}'.format(oct(num)))
elif opção == 3:
    print('Seu numero em hexadecimal é {}'.format(hex(num)))
else:
    print('Você digitou um valor errado, por favor tente novamente. ')


