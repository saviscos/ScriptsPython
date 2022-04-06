#Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
#de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
print('Bem vinde ao programa ESCREVENDO!')
i = int(input('Digite o número de 0 até 20: '))
while i > 20 or i < 20:
    i = int(input('Tente novamente. Digite o número de 0 até 20: '))
dados = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quartoze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
print(f'Você digitou o numero {dados[i]}')

