#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha
valores = [[],[], []]
n = 0
s = 0
p = 1
z = 0
m = 2
o = 0
pares = 0
terCol = 0
SegLin = 0
for v in range(1, 10):
    if v <= 3:
        valor = int(input(f'Digite o valor da posição {n,s}:'))
        valores[0].append(valor)
        if valor%2==0:
            pares = pares + valor
        if s == 1:
            SegLin = SegLin + valor
        s += 1
        if s == 3:
            terCol = terCol + valor
    if v>3 and v<7:
        valor = int(input(f'Digite o valor da posição {p, z}: '))
        valores[1].append(valor)
        if valor%2==0:
            pares = pares + valor
        if z == 1:
            if valor > SegLin:
                SegLin = valor
        z += 1
        if z == 3:
            terCol = terCol + valor
    elif v >= 7:
        valor = int(input(f'Digite o valor da posição {m, o}: '))
        valores[2].append(valor)
        if valor%2==0:
            pares = pares + valor
        if o == 1:
            if valor > SegLin:
                SegLin = valor
        o += 1
        if o == 3:
            terCol = terCol + valor
print(f'{valores[0][0]}  {valores[0][1]}  {valores[0][2]}\n{valores[1][0]}  {valores[1][1]}  {valores[1][2]}\n{valores[2][0]}  {valores[2][1]}  {valores[2][2]}')
print(f'O valor da soma de todos numeros pares é {pares}')
print(f'O valor da soma da terceira coluna é {terCol}')
print(f'O maior valor da segunda linha é {SegLin}')

#codJhon
listanum = [0, 1, 2]
listanova = []
seg = []
c = 0
d = 0
sompar = 0
tot = 0
somter = 0
while True:
for c in range (3):
listanova.append(int(input(f'Digite um valor para [{listanum[0]}, {listanum [c]}]: ')))
d += 1
if c == 2:
break
for c in range (3):
listanova.append(int(input(f'Digite um valor para [{listanum [1]}, {listanum [c]}]: ')))
d += 1
if c == 2:
break
for c in range (3):
listanova.append(int(input(f'Digite um valor para [{listanum [2]}, {listanum [c]}]: ')))
d += 1
if c == 2:
break
if d == 9:
break
for c in range (0, 9, 3):
print(f'[{listanova [c]:^5}] [{listanova [c + 1]:^5}] [{listanova [c + 2]:^5}]')
print('X' * 15)
for c in range (len(listanova)):
if listanova [c] % 2 == 0:
sompar += listanova [c]
tot += 1
somter = listanova [2] + listanova [5] + listanova [8]
for c in range (3, 6):
seg.append(listanova[c])
seg.sort()
print(f'A soma dos {tot} valores pares digitados é {sompar}.')
print(f'A soma dos valores da terceira coluna resulta em {somter}.')
print(f'O maior valor da segunda linha é {seg [-1]}')