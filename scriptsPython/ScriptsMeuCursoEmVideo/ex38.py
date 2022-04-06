#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais
num1 = int(input('Digite o primeiro numero inteiro:'))
num2 = int(input('Digite o segundo numero inteiro:'))
if num1 > num2:
    print('O primeiro valor digitado foi: {} e é MAIOR que o segundo valor digitado que foi {}'.format(num1,num2))
elif num1 < num2:
    print('O segundo valor digitado foi: {} e é MAIOR que o primeiro valor digitado que foi {}'.format(num2, num1))
elif num1 == num2:
    print('Os valores digitados foram {} e {} e são iguais'.format(num1,num2))
