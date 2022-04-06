valores = list()
for cont in range(0,5):
    valores.append(input('Digite um Valor:'))
print(valores)
menor = valores.index(min(valores))
maior = valores.index(max(valores))
valores.sort()
print(f'O menor valor foi {valores[0]} na posicão {menor + 1} e o maior valor foi o de {valores[4]} na posição {maior + 1}')
###
lista = []
for cont in range (0, 5):
lista.append(int(input('Digite um valor: ')))
lista2 = lista [:]
lista2.sort()
for c, v in enumerate(lista):
if lista2 [0] == lista [c]:
max = c
if lista2 [-1] == lista [c]:
min = c
print(f'O maior valor digitado foi {lista2 [0]}, na posição {max +1}.\nO menor valor digitado foi {lista2 [-1]}, na posição {min +1}.')

