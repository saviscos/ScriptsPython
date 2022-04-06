#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER
from datetime import date
anoatual = date.today().year
ano = int(input('Digite o ano de nascimento da atleta:'))
idade = anoatual - ano
if idade <= 9:
    print('O atleta tem {} anos e esta na categoria mirim'.format(idade))
elif idade > 9 and idade <= 14:
    print('O atleta tem {} anos e esta na categoria Infantil'.format(idade))
elif idade > 14 and idade <= 19:
    print('O atleta tem {} anos e esta na categoria Junior'.format(idade))
elif idade > 19 and idade <= 25:
    print('O atleta tem {} anos e esta na categoria Senior'.format(idade))
elif idade > 25:
    print('O atleta tem {} anos e esta na categoria Master'.format(idade))
