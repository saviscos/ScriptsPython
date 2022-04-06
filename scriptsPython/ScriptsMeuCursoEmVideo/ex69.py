#Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
mul20 = 0
pes18 = 0
homem = 0
while True:
    sexo = str(input('Digite o sexo da pessoa (M para masculino ou F para feminino):')).lower().split()[0]
    idade = int(input('Digite a idade da pessoa:'))
    if sexo[0] == 'm' or sexo[0] == 'f' :
        if sexo[0] == 'm':
            homem += 1
        if sexo[0] == 'f':
            if idade<20:
                mul20 += 1
        if idade > 18:
            pes18 += 1
        cont = str(input('Você quer inserir mais alguém na lista? [S/N]')).lower().split()[0]
        print('---'*15)
        if cont[0] == 'n':
            print('Obrigado por usar')
            break
    else:
        print('SEXO INVÁLIDO, tente novamente')
print('Existem {} homens presentes na lista'.format(homem))
print('Existem {} mulheres menores que 20 anos de idade'.format(mul20))
print('Existem {} pessoas maiores de 18 anos de idade'.format(pes18))

