#Exercício Python 080: Crie um programa onde o usuário possa digitar
# cinco valores numéricos e cadastre-os em uma lista, j
# já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.
#lista = []
#print (f'Bem vindo ao >ORDENADOR DE NÚMEROS<')
#lista = [int(input('Digite um valor: '))]
#print(lista [-1])
#for c in range (0, 4):
#    a = int(input('Digite outro valor: '))
#    if a >= lista [-1]:
#        lista.append(a)
#    elif a < lista [-1] and a > lista [0]:
#        lista.insert(1, a)
#    else:
#        lista.insert(0, a)
#print(f'Este é a lista em ordem crescente dos valores adicionados: {lista}')

lista = []
for c in range(5):
    n = int(input('Número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('O número foi adicionado no final da lista.')
    else:
        for i in range(5):
            if n <= lista[i]:
                lista.insert(i,n)
                print(f'O número foi adicionado na posição {i}.')
                break
print(lista)