#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e
# preencha com valores lidos pelo teclado.
#o final, mostre a matriz na tela, com a formatação correta.
valores = [[],[], []]
n = 0
s = 0
p = 1
z = 0
m = 2
o = 0
for v in range(1, 10):
    if v <= 3:
        valor = int(input(f'Digite o valor da posição {n,s}:'))
        valores[0].append(valor)
        s += 1
    if v>3 and v<7:
        valor = int(input(f'Digite o valor da posição {p, z}: '))
        valores[1].append(valor)
        z += 1
    elif v >= 7:
        valor = int(input(f'Digite o valor da posição {m, o}: '))
        valores[2].append(valor)
        o += 1
print(f'{valores[0][0]}  {valores[0][1]}  {valores[0][2]}\n{valores[1][0]}  {valores[1][1]}  {valores[1][2]}\n{valores[2][0]}  {valores[2][1]}  {valores[2][2]}')

