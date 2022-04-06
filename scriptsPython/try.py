lista = [1,10]
arquivo = open('teste.txt','r')
try:
    divisão = 10 / 1
    numero = lista[1]
    print
except ZeroDivisionError:
    print('Não é possivel realizar divisão por zero')
except IndexError:
    print('Erro ao acessar um indice inválido')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executou, pois sem erros')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()

