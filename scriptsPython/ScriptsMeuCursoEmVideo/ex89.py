#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e
#guarde tudo em uma lista composta. No final, mostre um boletim
#contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
lista = []
listacomplexa = []
numalunos = 0
while True:
    nome = str(input('Digite o nome do Aluno:')).upper()
    numalunos = numalunos + 1
    lista.append(nome)
    nota1 = float(input('Digite a primeira nota do Aluno:'))
    nota2 = float(input('Digite a segunda nota do Aluno:'))
    media = (nota1 + nota2)/2
    lista.append(nota1)
    lista.append(nota2)
    lista.append(media)
    listacomplexa.append(lista[:])
    lista.clear()
    cont = input('Você quer continuar? (S/N):').lower()
    if cont == 'n':
        break
for c in range(0,numalunos):
    print(f'O aluno {listacomplexa[c][0]} teve nota com média {listacomplexa[c][3]}')
    print('-'*16)
while True:
    continuar = input('Você quer ver a nota de algum aluno? (S/N):').lower()
    if continuar == 'n':
        break
    for c in range(0, numalunos):
        nomealuno = input('De qual aluno você quer obter a nota?').upper()
        if nomealuno == listacomplexa[c][0]:
            print(f'As notas do aluno {listacomplexa[c][0]} foram {listacomplexa[c][1]} e {listacomplexa[c][2]}')
            break