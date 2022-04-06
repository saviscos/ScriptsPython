#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
from random import sample
todosvalores = []
valores = []
jogos = int(input('Quantos jogos serão gerados?'))
for c in range(0, jogos):
    a = sorted(sample(range(1, 61), 6))
    todosvalores.append(a[:])
    a.clear()
for c in range(0, jogos):
    print(f'O jogo numero {c + 1} foi {todosvalores[c]}')



