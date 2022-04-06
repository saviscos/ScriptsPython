nomes = []
pesos = []
listpes = []
listlev = []
while True:
nomes.append(str(input('Nome: ')))
pesos.append(float(input('Peso: ')))
quest = str(input('Deseja continuar [S/N]? ')).strip().upper()
if quest [0] == 'N':
break
manipulação = pesos [:]
manipulação.sort()
cont = 0
for c in pesos:
if c == manipulação [-1]:
listpes.append(nomes [cont])
listpes.append(pesos [cont])
if c == manipulação [0]:
listlev.append(nomes [cont])
listlev.append(pesos [cont])
cont += 1
print(f'O maior peso cadastrado foi {listpes [0]} de {listpes [1]}.')
print(f'O menor peso cadastrado foi {listlev [0]} de {listlev [1]}.')