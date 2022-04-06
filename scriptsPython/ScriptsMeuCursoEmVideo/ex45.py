#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
import random
from time import sleep
jk = str(input('Escolha entre Pedra, Papel e Tesoura:')).lower().strip()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*12)
sleep(1)
print('O escolhido por você foi {}'.format(jk))
sleep(1)
lista = ['Pedra','Papel','Tesoura']
pcjk = random.choices(lista)
pcjoke = str(pcjk)
print('O escolhido pelo computador foi {}'.format(pcjoke))
sleep(1)
if jk == 'pedra' and 'Pedra' in pcjoke:
    print('O jogo empatou, pois você escolheu Pedra e o Computador também')
elif jk == 'pedra' and 'Tesoura' in pcjoke:
    print('Você Ganhou, pois você escolheu Pedra e o Computador escolheu Tesoura')
elif jk == 'pedra' and 'Papel' in pcjoke:
    print('Você Perdeu, pois você escolheu Pedra e o Computador escolheu Papel')
elif jk == 'papel' and 'Pedra' in pcjoke:
    print('Você ganhou, pois você escolheu Papel e o Computador escolheu Pedra')
elif jk == 'papel' and 'Tesoura' in pcjoke:
    print('Você perdeu, pois você escolheu papel e o Computador escolheu Tesoura')
elif jk == 'papel' and 'Papel' in pcjoke:
    print('Deu empate, pois você escolheu Pedra e o Computador escolheu Papel')
elif jk == 'tesoura' and 'Pedra' in pcjoke:
    print('Você perdeu, pois você escolheu tesoura e o Computador escolheu Pedra')
elif jk == 'tesoura' and 'Tesoura' in pcjoke:
    print('Você empatou, pois você escolheu tesoura e o Computador escolheu Tesoura')
elif jk == 'tesoura' and 'Papel' in pcjoke:
    print('Deu ganhou, pois você escolheu Tesoura e o Computador escolheu Papel')
else:
    print('Escolha errada. Escolha entre Pedra, Papel e Tesoura')
