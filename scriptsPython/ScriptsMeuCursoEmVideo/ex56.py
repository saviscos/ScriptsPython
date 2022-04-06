#Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
media = 0
mediacomp = media / 4
maior = 0
mulheres = 0
homem = 0
for i in range(1,5):
    nome = str(input('Digite o nome:'))
    idade = int(input('Digite a idade:'))
    sexo = str(input('Digite o sexo da pessoa (M para masculino ou F para feminino):')).lower()
    media = media + idade
    if 'm' in sexo:
        if idade>maior:
            idade = maior
            nomemai = nome
            homem = homem + 1
    if 'f' in sexo:
        if idade<20:
            mulheres = mulheres + 1
if homem >= 1:
    print('O nome da pessoa mais velha é {}'.format(nomemai))
else:
    print('Não existem dados de homens mais velhos pois não há homens na lista')
mediacomp = media / 4
print('A media das idades é {}'.format(mediacomp))
print('A quantidade de mulheres menores que 20 é {}'.format(mulheres))
