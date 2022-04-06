#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro,
#ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
valores = list()
while True:
    val = int(input('Digite um valor:'))
    if val in valores:
        print('Este valor já foi adicionado')
    else:
        valores.append(val)
    cont = str(input('Você quer continuar adicionando numeros? (S/N): \n')).upper()[0]
    if cont != 'S':
        break
valores.sort()
print(f'A sua lista de valores foi: {valores}')
