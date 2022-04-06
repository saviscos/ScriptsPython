from random import randint
itens = ('Pedra','Tesoura','Papel')
computador = randint(0,2)
print('O computador escolheu {}'.format(itens[computador]))
