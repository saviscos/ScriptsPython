#Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.
numero = int(input('Digite um numero de 0 a 9:'))
for c in range(0,10):
    print('A tabuada do numero {} e {} é: {}'.format(numero,c,numero*c))
