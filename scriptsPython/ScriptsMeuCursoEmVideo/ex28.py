####ex28 exercicios 028 : Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. programa deverá escrever na tela se o usuário venceu ou perdeu.
#import random
#n1 = int(input('Digite um numero inteiro de 0 a 5:'))
#n2 = int(random.randint(0,5))
#print('O número que o computador pensou foi: {} e o que você digitou foi {}'.format(n2, n1))
#print('O numero foi o mesmo, você ganhou' if n1==n2 else 'O numero foi diferente, você perdeu')


#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
#vel = int(input('Digite a velocidade que o carro estava:'))
#if vel > 80:
#    acima = vel - 80
#    multa = acima * 7
#    print('O carro foi mutado, sua velocidade foi de {}km/h, sua velocidade estava {}km/h acima do permitido e sua multa foi de {} reais'.format(vel,acima,multa))
#else:
#    print('O carro estava na velocidade permitida')

#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
#n = float(input('Digite um numero inteiro:'))
#if n%2 == 0:
#    print('Este numero é par')
#else:
#    print('Este numero é impar')
#n = str(input('Digite um número: ')).replace('',' ').split()
#print(n)
#c = n[-1]
#print(c)
#l = ["0","2","4","6","8"]
#print('Par' if c in l else 'Impar')

#Outro
#import random, emoji, time
#n = random.randint(0, 5)
#print('----' * 10)
#m = int(input(emoji.emojize('Eu pensei em um número de 0 à 5!! :eye::eye:\nSerá que você consegue descobrir qual foi? :eyes:\nDigite seu palpite :ghost: : ', use_aliases=True, variant="emoji_type")))
#print('----' * 10)
#print('Processando...')
#time.sleep(2)
#print(emoji.emojize('Parabéns, você ganhou! :imp:', use_aliases=True, variant="emoji_type") if m == n  else emoji.emojize('Ah, que pena! Você errou. :smiling_imp: \nEu pensei no {} e você no {}. Tente novamente... :game_die:'.format(n,m), use_aliases=True, variant="emoji_type"))

#031 Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
#d = int(input('Distancia da viagem:'))
#if d <= 200:
#    passagem = d * 0.5
#    print('A passagem foi de {} reais'.format(passagem))
#else:
#    passagem = d * 0.45
#    print('A passagem foi de {} reais'.format(passagem))

#Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano = int(input('Digite um ano, Coloque zero pra o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano%4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))




