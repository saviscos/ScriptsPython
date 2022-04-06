#Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida
peso = int(input('Adicione o valor do peso:'))
altura = float(input('Adicione o valor da altura em metros:'))
imc = peso / (altura**2)
print('O IMC da pessoa é {:2f}'.format(imc))
if imc < 18.5:
    print('A pessoa esta abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('A pessoa esta no peso ideal')
elif imc >= 25 and imc < 30:
    print('A pessoa esta com sobrepeso')
elif imc >= 30 and imc < 40:
    print('A pessoa esta com obesidade')
else:
    print('A pessoa esta com Obesidade Mórbida')
