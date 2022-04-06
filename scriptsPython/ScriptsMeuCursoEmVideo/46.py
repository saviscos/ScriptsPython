#Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
#indo de 10 até 0, com uma pausa de 1 segundo entre eles.
#from time import sleep
#for c in range(10, 0, -1):
#    sleep(1)
#    print(c)
#print('FELIZ FOGOS NO CU')

import time
import emoji
print('Você está preparado para queima de FOGOS?\nVAMOS LA!!!')
for c in range (10, 0, -1):
    print(c)
    time.sleep(1)
print(emoji.emojize(':fireworks: KABOOOMMM!!:fireworks:'))
