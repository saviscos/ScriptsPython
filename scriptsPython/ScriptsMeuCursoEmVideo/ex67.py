#Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez,
#para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
#while True:
#    tab = int(input('Você quer a tabuada de qual numero? [Digite um valor negativo para parar] :'))
#    if tab < 0:
#        break
#    print(tab, 'x 1', '=', tab*1, '\n', tab, 'x 2', '=', tab*2, '\n', tab, 'x 3', '=', tab*3, '\n', tab, 'x 4', '=', tab*4, '\n', tab, 'x 5', '=', tab*5, '\n', tab, 'x 6', '=', tab*6, '\n', tab, 'x 7', '=', tab*7, '\n', tab, 'x 8', '=', tab*8, '\n', tab, 'x 9', '=', tab*9, '\n', tab, 'x 10', '=', tab*10, '\n')

while True:
    n = int(input('Digite um numero:'))
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
