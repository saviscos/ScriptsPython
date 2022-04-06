#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO
n1 = float(input('Digite a nota da primeira avaliação:'))
n2 = float(input('Digite a nota da segunda avaliação:'))
media = (n1+n2)/2
if media == 7 or media > 7:
    print('Sua média foi {} e você foi APROVADO'.format(media))
elif media < 5:
    print('Sua média foi {} e você foi REPROVADO, boa sorte na proxima'.format(media))
elif media >= 5 or media <= 6.9:
    print('Sua média foi {} e você esta de RECUPERAÇÃO'.format(media))
