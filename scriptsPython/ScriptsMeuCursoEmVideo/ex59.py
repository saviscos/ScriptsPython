#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
print('Bem vindo ao seu SaviscoOperator')
num1 = int(input('Digite o primeiro valor:'))
num2 = int(input('Digite o segundo valor:'))
print('---'*10)
print('''Escolha qual operação você quer fazer:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
opcao = int(input('Digite uma das opções acima:'))
while opcao != 5:
    if opcao == 1:
        soma = num1 + num2
        print('A soma dos valores {} e {} foi de {}'.format(num1,num2,soma))
        print('''Escolha qual operação você quer fazer:
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa''')
        opcao = int(input('Digite uma das opções acima:'))
    elif opcao == 2:
        mult = num1 * num2
        print('A multiplicação dos valores {} e {} foi de {}'.format(num1,num2,mult))
        print('''Escolha qual operação você quer fazer:
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa''')
        opcao = int(input('Digite uma das opções acima:'))
    elif opcao == 3:
        if num1 > num2:
            print('O valor {} é MAIOR que o {}'.format(num1,num2))
            print('''Escolha qual operação você quer fazer:
            [ 1 ] somar
            [ 2 ] multiplicar
            [ 3 ] maior
            [ 4 ] novos números
            [ 5 ] sair do programa''')
            opcao = int(input('Digite uma das opções acima:'))
        elif num1 < num2:
            print('O valor {} é MAIOR que o {}'.format(num2,num1))
            print('''Escolha qual operação você quer fazer:
            [ 1 ] somar
            [ 2 ] multiplicar
            [ 3 ] maior
            [ 4 ] novos números
            [ 5 ] sair do programa''')
            opcao = int(input('Digite uma das opções acima:'))
        elif num1 == num2:
            print('Os valores digitados foram iguais. Ambos são {}'.format(num1))
            print('''Escolha qual operação você quer fazer:
                        [ 1 ] somar
                        [ 2 ] multiplicar
                        [ 3 ] maior
                        [ 4 ] novos números
                        [ 5 ] sair do programa''')
            opcao = int(input('Digite uma das opções acima:'))
    elif opcao == 4:
        num1 = int(input('Digite o primeiro valor:'))
        num2 = int(input('Digite o segundo valor:'))
        print('''Escolha qual operação você quer fazer:
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa''')
        opcao = int(input('Digite uma das opções acima:'))
    else:
        print('Opção Invalida')
        opcao = int(input('Digite uma das opções acima:'))
print('Você saiu do Programa, obrigado por utilizar o SaviscoOperator')


