#arquivo = open('arquivo.txt','r+')
#print('Abrindo com Read\n')
#print(arquivo.read())

#arquivo.seek(0)

#print('Abrindo com Readline\n')
#print(arquivo.readline())

#arquivo.seek(0)

#print('Abrindo com Readlines\n')
#print(arquivo.readlines())

#arquivo.close()

#print('Teste 2 - abertura de arquivos')
#file = open('arquivo.txt','r')
#for linha in file:
#    linha = linha.rstrip()
#   print(linha)
#file.close()

#file = open('arquivo.txt','r')
#contador = 0
#for linha in file:
#    contador += 1
#print(contador)

#palavra = input('Digite a palavra:')
#arq = open('arquivo.txt','r')
#contador = 0
#for linha in arq:
#    linha = linha.rstrip()
#    if palavra in linha:
#        contador += 1
#        print(linha)
#print(contador)
#arq.close()

#arquivo = open('teste.txt','r+')
#arquivo.write('''Treinando aqui \n E sobre isso e ta tudo bem \n Bora jogar TfT depois''')
#print(arquivo.read())

#arquivo = open('test.txt','w')
#arquivo.write('''Treinando aqui \n E sobre isso e ta tudo bem \n Bora jogar TfT depois''')
#arquivo.close()
#arq = open('test.txt','r')
#for linha in arq:
#   linha = linha.rstrip()
#    print(linha)
#arq.close()

print('\n')
texto = input('Escreva aqui o texto:')
arquivo = open('test.txt','a')
arquivo.write(texto + "\n")
print('Concluido!' + arquivo.name)
arquivo.close()

arquivo = open('test.txt','r')
for linha in arquivo:
    linha = linha.rstrip()
    print(linha)
arquivo.close()



