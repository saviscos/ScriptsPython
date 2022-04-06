#Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
# Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.
campeonato = ('Atlético-MG','Palmeiras', 'Fortaleza', 'Flamengo','Bragantino', 'Corinthians','Internacional', 'Fluminense',
			  'Athletico-PR','Cuiabá','Ceará','Atlético-GO','São Paulo','Juventude','América-MG','Santos','Bahia','Grêmio'
			  ,'Sport','Chapecoense')
#for c in campeonato:
#	print(f'Os cinco primeiros colocados são: {campeonato[0:5]}')
print('Lista dos CINCO MELHORES colocados do campeonato brasileiro:\n')
for cont in range(0, 5):
    print(f'O {cont + 1}º colocado do campeonato brasileiro é o {campeonato[cont]}')
print('\nLista dos QUATRO ULTIMOS colocados do campeonato brasileiro:\n')
for cont in range(16, 20):
    print(f'O {cont + 1}º colocado do campeonato brasileiro é o {campeonato[cont]}')
print('\nLista dos times do campeonato brasileiro EM ORDEM ALFABÉTICA:\n')
camp2 = sorted(campeonato)
for c in camp2:
    print(f'{c}')
print('\nColocação do CHAPECOENSE:\n')
chape = campeonato.index('Chapecoense')
print(f'O time Chapecoense esta na posição {chape + 1}')
