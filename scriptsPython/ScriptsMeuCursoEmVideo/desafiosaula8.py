#desafio 16 crie um programa que mostre leia num numero real que mostra a parte inteira
#import math
#num = float(input('Digite um numero com mais fracionario com mais de 3 digitos:'))
#print('A parte inteira do numero {} é {}'.format(num,math.trunc(num)))

#desafio 017 cateto oposto e cateto adjacente e mostra a hipotenuca
#import math
#ops = int(input('Insira o cateto oposto'))
#adj = int(input('Insira o cateto adjacente'))
#hip = math.sqrt(ops**2 + adj**2)
#print('O valor da hipotenusa é {}'.format(hip))

#desafio 18 ler um angulo e mostrar seu sen, cos, e tg
#import math
#angrad = int(input('Digite um angulo:'))
#ang = math.radians(angrad)
#print('o valor do angulo digitado é {}, seu seno é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}'.format(ang, math.sin(ang), math.cos(ang), math.tan(ang)))

#desafio 19 ler 4 nomes e sortear um
#import random
#nome1 = input('digite o primeiro aluno:')
#nome2 = input('digite o segundo aluno:')
#nome3 = input('digite o terceiro aluno:')
#nome4 = input('digite o quarto aluno:')
#lista = nome1,nome2,nome3,nome4
#print('O nome sorteado foi {}'. format(random.choice(lista)))

#desafio 20 ler 4 nomes e dar uma ordem de apresentação aleatoria
#from pygame import mixer
#mixer.init()
#mixer.music.load('musica.mp3')
#mixer.music.play()
#input('Agora você escuta?')

from playsound import playsound
playsound('musica.mp3')






