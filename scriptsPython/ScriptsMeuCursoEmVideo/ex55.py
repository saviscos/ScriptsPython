#Python 055: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
#lst=[]  #lista vazia
#for c in range(1, 6):
#    peso=float(input('Peso da {}ª pessoa: '.format(c)))
#    lst+=[peso]   #adc os valores de peso na lista
#print('O Maior peso foi:', max(lst))  #maximo valor da lista
#print('O Menor peso foi:', min(lst))  #minimo valor da lista

#maior = 0
#menor = float('inf')
#for i in range(5):
#    p = float(input('Peso: '))
#    if p>maior:
#        maior = p
#    if p<menor:
#        menor = p
#print(f'Dentre esses, o maior peso foi {maior}kg e o menor foi {menor}kg ')

maior = 0
menor = 0
for i in range(1,6):
    peso = float(input('Pesito:'))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi {} e o menor peso foi {}'.format(maior, menor))

