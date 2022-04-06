#Exercício Python 066: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag)
cont = 0
quant = 0
while True:
    num = int(input('Digite um numero [Digite 999 para parar]:'))
    if num == 999:
        break
    cont += num
    quant += 1
print(f'Foram digitados {quant} numeros e a soma deles foi {cont}')
