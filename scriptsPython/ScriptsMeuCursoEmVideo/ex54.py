#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime
from datetime import date
contmaior = 0
contmenor = 0
ano_atual = date.today().year
for c in range(0,7):
    nasc = int(input('Digite o ano de nascimento:'))
    if nasc > ano_atual :
        print('A data de nascimento é inválida')
    elif nasc < ano_atual - 110:
        print('A data de nascimento é de alguém que já veio a óbito')
    idade = ano_atual - nasc
    if idade > 18:
        contmaior = contmaior + 1
    else:
        contmenor = contmenor + 1
print('''A quantidade de pessoas MAIORES de idade que 18 são {}.\n 
E a quantidade de pessoas MENORES de idade são: {}'''.format(contmaior,contmenor))



