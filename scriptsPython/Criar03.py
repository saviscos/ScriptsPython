def escrever_arquivo(texto):
    #diretorio = 'C:'
    arquivo = open('Teste.txt', 'w')
    arquivo.write('texto')
    arquivo.close()

def atualizar_arquivo(nome_arquivo,texto):
    arquivo = open(nome_arquivo,'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    texto = arquivo.read()
    print(texto)
def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        print(lista_notas)
        aluno = lista_notas[0]
        lista_notas.pop(0)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

#def copia_arquivo(nome_arquivo):
#    import shutil
#    shutil.copy(nome_arquivo,'C:Diretorio')


if __name__ == '__main__':
    lista_media = media_notas('notas.txt')
    media_notas('notas.txt')
    #escrever_arquivo('Primeira linha.\n')
    aluno = '\nFelipe,7,8,5,6'
    atualizar_arquivo('notas.txt',aluno)
    #ler_arquivo('Teste.txt')


