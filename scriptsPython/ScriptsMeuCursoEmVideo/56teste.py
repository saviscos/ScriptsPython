media = 0
maior = 0
for i in range(1,5):
    nome = str(input('Digite o nome:'))
    idade = int(input('Digite a idade:'))
    sexo = str(input('Digite o sexo da pessoa (M para masculino ou F para feminino):')).lower()
    media = media + idade
    if sexo == 'm':
        if idade > maior:
            maior = idade

print(name)


#print('O nome da pessoa de sexo masculino mais velho é {}'.format(nome[a]))
#mediacomp = media / 4
#print('A media das idades é {}'.format(mediacomp))
