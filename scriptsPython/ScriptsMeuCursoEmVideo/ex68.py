#Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador perder,
#mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
#import random
#l = ['pedra', 'papel', 'tesoura']
#vitoria = 0
#while True:
#    jogador = str(input('Escolha entre Pedra, Papel ou Tesoura:')).lower().strip()
#    machine = str(random.choice(l))
#    print(f'O computador escolhei {machine}')
#    if jogador in machine:
#        print(f'O jogo deu empate, ambos escolheram {jogador}')
#    if 'papel' in jogador and 'pedra' in machine:
#        print(f'Você GANHOU, pois {jogador} cobre {machine}')
#        vitoria += 1
#    if jogador == 'papel' and machine == 'tesoura':
#        print(f'Você PERDEU, pois  {jogador} é cortada por {machine}, você ganhou {vitoria} vezes')
#        print('Tente Novamente')
#        break
#    if jogador == 'pedra' and machine == 'tesoura':
#        print(f'Você GANHOU, pois você escolheu {jogador} que quebra a {machine}')
#        vitoria += 1
#    if jogador == 'pedra' and machine == 'papel':
#        print(f'Você PERDEU, pois você escolheu {jogador} que é coberto por {machine}, você ganhou {vitoria} vezes')
#        print('Tente Novamente')
#        break
#    if jogador == 'tesoura' and machine == 'papel':
#        print(f'Você GANHOU, pois você escolheu {jogador} que corta {machine}')
#        vitoria += 1
#    if jogador == 'tesoura' and machine == 'pedra':
#       print(f'Você PERDEU, pois você escolheu {jogador} que é quebrado por {machine}, você ganhou {vitoria} vezes')
#        print('Tente Novamente')
#        break

import random, time
vc = 0
print('Bem vindo ao jogo PAR OU IMPAR?')
while True:
    des = str(input('Você quer par ou impar? ').strip().lower())
    num = int(input('Digite um número: '))
    numpc = random.randint(1,10)
    print('PAR OU IMPAAAR...')
    time.sleep(1)
    soma = num + numpc
    print(f'Você jogou {num} e eu joguei {numpc}... {soma} é:', end='')
    if soma %2 == 0:
        print('PAR')
        if des [0] == 'p':
            print('Você ganhou!!')
            vc += 1
        else:
            print('Você perdeu!! Tente novamente!')
            break
    else:
        print('IMPAR')
        if des [0] == 'i':
            print('Você ganhou!!')
            vc += 1
        else:
            print('Você perdeu!!')
            break
if vc != 0:
    print(f' você ganhou {vc} vezes consecutivas!!')
else:
    print('Obrigado por jogar!')

