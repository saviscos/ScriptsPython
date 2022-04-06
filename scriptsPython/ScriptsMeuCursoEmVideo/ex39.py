#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
anoatual = date.today().year
ano = int(input('Digite o ano de nascimento:'))
idade = anoatual - ano
print ('A idade da pessoa é {}'.format(idade))
if idade > 18:
    tempo = idade - 18
    print('''O tempo pra se alistar já passou!!
    Você esta atrasado {} anos'''.format(tempo))
elif idade < 18:
    tempo2 = 18 - idade
    print('''Você ainda pode se alistar!!!
    Você está adiantado {} anos'''.format(tempo2))
elif idade == 18:
    print('Você tem 18 anos! Bem vindo ao alistamento')
