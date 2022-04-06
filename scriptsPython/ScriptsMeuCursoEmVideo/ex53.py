#Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.
#pal1 = str(input('Digite uma frase:')).strip().replace(' ','')
#tam1 = len(pal1)
#pal2 = [pal1[::-1]]
#print(pal2)
#tam2 = len(pal2)
#if pal1 in pal2:
#   print('É um palindromo')
#else:
#    print('Não é um palindromo')


#frase = str(input('Digite uma frase:')).lower().strip()
#palavras = frase.split()
#print(palavras)
#junto = ''.join(palavras)
#print(junto)
#tam = len(junto)
#print(tam)
#inverso = ''
#for letra in range(tam - 1, -1, -1): #Inverter
#    inverso += junto[letra] #Variavel inverso recebe invertido
#print(junto, inverso)
#if inverso==sopa:
#    print('É um palindromo')
#else:
#    print('Não é um palindromo')

print('DETECTOR DE PALINDROMO')
fra = str(input('Digite uma frase: ')).lower().strip()
fram = fra.replace('', ' ').split()
n = len(fram)
frainv = fram[::-1]
cont = 0
for c in range (n-1, -1, -1):
    if fram[c] == frainv[c]:
        cont+=1
if cont == n:
    print('{} é uma frase palindroma'.format(fra))
else:
    print('{} não é uma frase palindroma'.format(fra))



