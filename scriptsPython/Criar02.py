def escrever_arquivo(texto):
    #diretorio = 'C:'
    arquivo = open('Teste.txt', 'w')
    arquivo.write('texto')
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('Teste.txt','a')
    arquivo.write(texto)
    arquivo.close()
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    texto = arquivo.read()
    print(texto)

if __name__ == '__main__':
    escrever_arquivo('Primeira linha.\n')
    #atualizar_arquivo('Segunda linha.\n')
    ler_arquivo('Teste.txt')