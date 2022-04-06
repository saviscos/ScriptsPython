#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um
# número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

#import random
#list = [0,1,2,3,4,5,6,7,8,9,10]
#aleatorio = random.choice(list)
#escolhido = int(input('Escolha um numero de 0 a 10:'))
#cont = 1
#while aleatorio != escolhido:
#    escolhido = int(input('Escolha um numero de 0 a 10:'))
#    cont = cont + 1
#print('Você acertou!! Você tentou {} vezes'.format(cont))

#import random, time
#n = random.randint(0,10)
#c = 0
#s = 0
#print('Bem vindo ao jogo \33[4mDESCUBRA MEU NÚMERO!\33[m')
#print('Irei pensar em um número de 0 à 10, será que você consegue descobrir qual é?')
#print('Pensando...')
#time.sleep(2)
#while s != n:
#    s = int(input('Digite o seu palpite: '))
#    print('\33[31mNão foi esse, tente novamente!!\33[m')
#    c +=1
#print('\33[33mVocê descobriu!! Só foram necessárias {} tentativas!\33[m'.format(c))

from random import randint
from time import sleep
computador = randint(0, 10)
print('Sou seu computador...Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Tente um número maior!')
        elif jogador > computador:
            print('Tente um número menor!')
print('Analisando...'), sleep(3)
print('Você acertou com {} tentativas! Parabéns'.format(palpites))