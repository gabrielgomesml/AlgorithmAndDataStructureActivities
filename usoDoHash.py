class ListaLigada:
    def __init__(self, chave, valor, esquerda=None):
        self.chave = chave
        self.valor = valor
        self.esquerda = esquerda

class Hash:
    def __init__(self):
        self.tabelaHash = [None] * 30

    def funcaoHash(self, chave):
        return chave % 31

    def inserir(self, chave, valor):
        chaveDoHash = self.funcaoHash(chave)
        if not self.tabelaHash[chaveDoHash]:
            self.tabelaHash[chaveDoHash] = ListaLigada(chaveDoHash, valor)
        else:
            ultimo = self.tabelaHash[chaveDoHash]
            while ultimo.esquerda:
                ultimo = ultimo.esquerda
            ultimo.esquerda = ListaLigada(chaveDoHash, valor)
        return self.tabelaHash
                
def pegarNomes(lista):
    lista = lista[:len(lista) -1]
    lista = [' '.join(lista)]
    return lista
    

def aniversarios(arquivo):
    arq = open(arquivo, 'r')
    database = arq.readlines()
    for x in range(len(database)):
        database[x] = database[x].strip()
        database[x] = database[x].split()
    aux = 0
    while aux < len(database):
        i = 0
        while database[aux][i] not in [str(x) for x in range(1, 32)]:
            i += 1
        database[aux] = database[aux][:i+1]
        aux += 1

    hash_table = Hash()
    for y in database:
        hash_table.inserir(int(y[len(y) -1]), pegarNomes(y))

    for i in range(len(hash_table.tabelaHash)):
        aux = hash_table.tabelaHash[i]
        if aux:
            print('Dia: ' + str(aux.chave))
            while aux:
                print(aux.valor[0][:len(aux.valor[0])-1])
                aux = aux.esquerda

if __name__ == '__main__':
    nomeDoArquivo = input("Nome do arquivo(digite com o .txt no final): ")
    aniversarios(nomeDoArquivo)

# Como nosso objetivo é mapear os dias de aniver´sario, é interessante utilizar os príncipios de hash function e
# hash code para fazer a alocação dos itens em seus respectivos locais. Paralelamente, haverá divesas colisões
# nesses "endereços', o que nos leva a dar preferencia a uma tabela de Endereçamento Fechado, que apesar de
# ser pouco viável à eliminação de conteúdo, como esse não é nosso foco, podemos usar a lógica da Lista Ligada.
# Ou seja, elementos que tiverem o mesmo hash codes, serão ligados um a um.
#
# [0]-[Elemento1] --> [Elemento2] --> [Elemento3] --> [Elemento4]
# [1]-[Elemento1]
# [2]-[Elemento1] --> [Elemento2]
# [3]-[Elemento1]
# [4]-[None]
# [5]-[Elemento1] --> [Elemento2] --> [Elemento3]