#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes
l1 = int(input('Digite o valor do primeiro lado:'))
l2 = int(input('Digite o valor do segundo lado:'))
l3 = int(input('Digite o valor do terceiro lado:'))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print(f'Os lados {l1}, {l2}, {l3} PODEM formar um triângulo!!')
    if l1 == l2 and l2 == l3 and l3 == l1:
        print('O triangulo é equilatero')
    elif l1 == l2 and l3 != l1 and l3 != l2:
        print('O triangulo é isoceles')
    elif l1 == l3 and l2 != l1 and l2 != l1:
        print('O triangulo é isoceles')
    elif l2 == l3 and l3 != l1 and l1 != l2:
        print('O triangulo é isoceles')
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print('O triangulo é escaleno')
else:
    print(f'Os lados {l1}, {l2}, {l3} NÂO PODEM formar um triângulo!!')

