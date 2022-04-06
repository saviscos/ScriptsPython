#Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e
# mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
#print(f'{" SEQUÊNCIA DE FIBONACCI ":=^50}')
#n = int(input('Quantos termos quer mostrar da sequência: '))
#c = 0
#segundo = c
#proximo = 1
#print('0', end='')
#while c <= n - 2:
#    print(f' → {proximo}', end='')
#    c += 1
#   proximo += segundo
#    segundo = proximo - segundo
#print(' → FIM')

#Nant = 1
#Fibonacci = 0
#n = int(input('Digite um número:(Este vai ser o nº de elementos da sequência) '))
#while n != 0:
#    print('{}'.format(Fibonacci), end=' → ')
#    Fibonacci = Fibonacci + Nant
#    Nant = Fibonacci - Nant
#    n -= 1
#print('FIM')

print('-'*30)
print('SEQUENCIA DE FIBONACCI')
print('-'*30)
n = int(input('Quantos termos você quer mostrar?'))
t1 = 0
t2 = 1
print('~'*30)
print('{} → {}'.format(t1,t2), end = '')
cont = 3
while cont <= n:
    t3 = t2 - t1
    print('→ {}'.format(t3), end '')
    t1 = t2
    t2 = t3
    cont =+ 1
print('→ FIM')




