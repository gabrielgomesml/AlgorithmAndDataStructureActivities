class GrafoLista:
    def __init__(self, iteravel, ponderado=False, direcionado=False):
        self.iteravel = iteravel
        self.ponderado = ponderado
        self.direcionado = direcionado
        self.listaDeAdj = {}
        self.criarListas(iteravel, ponderado, direcionado)

    def __str__(self):
        for x in self.listaDeAdj:
            print(str(x) + ': ' + str(self.listaDeAdj[x]))

    def __repr__(self):
        return 'GrafoLista(' + str(self.iteravel) + ')'

    def __getItem__(self, index):
        if not index in self.listaDeAdj:
            return '[' + str(index) + '] não encontrado.'
        return self.listaDeAdj[index]

    def ligados(self, tupla):
        if type(tupla) is int:
            return '[' + str(tupla) + '] não encontrado. Formato inválido.'
        if tupla[0] not in self.listaDeAdj or tupla[1] not in self.listaDeAdj:
            return '[' + str(tupla) + '] não encontrado. Par não existente nessa tupla.'
        if not self.ponderado:
            if tupla[1] in self.listaDeAdj[tupla[0]] or tupla[0] in self.listaDeAdj[tupla[1]]:
                return True
        elif self.ponderado:
            for x in self.listaDeAdj[tupla[0]]:
                if tupla[1] is x[0]:
                    return True
            for x in self.listaDeAdj[tupla[1]]:
                if tupla[0] is x[0]:
                    return True
        return False

    def grauDeSaida(self, vertice):
        if not vertice in self.listaDeAdj:
            return '[' + str(vertice) + '] não encontrado.'
        return len(self.listaDeAdj[vertice])

    def grauDeEntrada(self, vertice):
        if not vertice in self.listaDeAdj:
            return '[' + str(vertice) + '] não encontrado.'
        aux = 0
        if not self.ponderado:
            for x in self.listaDeAdj:
                if vertice in self.listaDeAdj[x]:
                    aux += 1
        elif self.ponderado:
            for x in self.listaDeAdj:
                for y in self.listaDeAdj[x]:
                    if vertice is y[0]:
                        aux += 1
        return aux

    def adjacente(self, vertice):
        if not vertice in self.listaDeAdj:
            return '[' + str(vertice) + '] não encontrado.'
        return self.listaDeAdj[vertice]

    def maiorAresta(self):
        if not self.ponderado:
            return 'Grafo não-ponderado.'
        maiores = []
        aux = 0
        for x in self.listaDeAdj:
            for y in self.listaDeAdj[x]:
                if y[1] > aux:
                    aux = y[1]
        for x in self.listaDeAdj:
            for y in self.listaDeAdj[x]:
                if y[1] == aux :
                    maiores.append((x, y[0]))
        return 'Arestas de peso: ' + str(aux) + ' // ' + 'Vértices ligados a ela: ' + str(maiores)

    def menorAresta(self):
        if not self.ponderado:
            return 'Grafo não-ponderado.'
        menores = []
        aux = 100000000000  #RevisarIssoAqui
        for x in self.listaDeAdj:
            for y in self.listaDeAdj[x]:
                if y[1] < aux:
                    aux = y[1]
        for x in self.listaDeAdj:
            for y in self.listaDeAdj[x]:
                if y[1] == aux :
                    menores.append((x, y[0]))
        return 'Arestas de peso: ' + str(aux) + ' // ' + 'Vértices ligados a ela: ' + str(menores)
        
    def adicionaVertice(self, vertice):
        #if type(tuple) is int:
            #return '[' + str(tupla) + '] não adicionado. Formato inválido.'
        #if self.ponderado and len(tupla) != 3:
            #return '[' + str(tupla) + '] não adicionado. Formato inválido para tuplas ponderadas.'
        #elif not self.ponderado and len(tupla) != 2:
            #return '[' + str(tupla) + '] não adicionado. Formato inválido para tuplas não-ponderadas.'
        #self.criarListas([tupla], self.ponderado, self.direcionado)

        if type(vertice) != int:
            return '[' + str(vertice) + '] não adicionado. Formato inválido.'
        if vertice in self.listaDeAdj:
            return '[' + str(vertice) + '] já existente.'
        else:
            self.listaDeAdj[vertice] = []
        

    def adicionaAresta(self, tupla):
        if type(tupla) is int:
            return '[' + str(tupla) + '] não adicionado. Formato inválido.'
        if self.ponderado and len(tupla) != 3:
            return '[' + str(tupla) + '] não adicionado. Formato inválido para tuplas ponderadas.'
        elif not self.ponderado and len(tupla) != 2:
            return '[' + str(tupla) + '] não adicionado. Formato inválido para tuplas não-ponderadas.'
        if tupla[0] not in self.listaDeAdj or tupla[1] not in self.listaDeAdj:
            return '[' + str(tupla) + '] não adicionado. Par não existente nessa tupla.'
        self.criarListas([tupla], self.ponderado, self.direcionado)
        if type(self.iteravel[0]) is tuple:
            self.iteravel += tuple(tupla),
        elif type(self.iteravel[0]) is list:
            self.iteravel.append(list(tupla))
        print('[' + str(tupla) + '] adicionada.')

    def removeAresta(self, tupla):
        if type(tupla) is int:
            return '[' + str(tupla) + '] não encontrado. Formato inválido.'
        elif len(tupla) != 2:
            return '[' + str(tupla) + '] não encontrado. Formato inválido.'
        if tupla[0] not in self.listaDeAdj or tupla[1] not in self.listaDeAdj:
            return '[' + str(tupla) + '] não removido. Par não existente nessa tupla.'
        if not self.direcionado:
            self.listaDeAdj[tupla[0]].remove(tupla[1])
            self.listaDeAdj[tupla[1]].remove(tupla[0])
        else:
            self.listaDeAdj[tupla[0]].remove(tupla[1])
        print('[' + str(tupla) + '] removida.')

    def criarListas(self, iteravel, ponderado, direcionado):
        if ponderado:
            for tupla in iteravel:
                origem, destino, peso = tupla
                if not origem in self.listaDeAdj:
                    self.listaDeAdj[origem] = []
                self.listaDeAdj[origem].append((destino, peso))
                if not direcionado:
                    if not destino in self.listaDeAdj:
                        self.listaDeAdj[destino] = []
                    self.listaDeAdj[destino].append((origem, peso))
        else:
            for tupla in iteravel:
                origem, destino = tupla
                if not origem in self.listaDeAdj:
                    self.listaDeAdj[origem] = []
                self.listaDeAdj[origem].append(destino)
                if not direcionado:
                    if not destino in self.listaDeAdj:
                        self.listaDeAdj[destino] = []
                    self.listaDeAdj[destino].append(origem)

    def dfs(self, v, antecessores, marcados):
        marcados[v] = True
        if self.ponderado:
            for x in self.adjacente(v):
                if not marcados[x[0]]:
                    antecessores[x[0]] = v
                    self.dfs(x[0], antecessores, marcados)
        else:
            for x in self.adjacente(v):
                if not marcados[x]:
                    antecessores[x] = v
                    self.dfs(x, antecessores, marcados)
        
    def buscaEmProfundidade(self):
        marcados = {}
        antecessores = {}
        for x in self.listaDeAdj:
            marcados[x] = False
            antecessores[x] = -1
        for v in marcados:
            if not marcados[v]:
                self.dfs(v, antecessores, marcados)
        return antecessores

    def buscaEmLargura(self):
        marcados = {}
        antecessores = {}
        vertices = []
        for x in self.listaDeAdj:
            marcados[x] = False
            antecessores[x] = -1
        for y in marcados:
            if not marcados[y]:
                vertices.append(y)
                marcados[y] = True
                while len(vertices) > 0:
                    v = vertices.pop(0)
                    if self.ponderado:
                        for z in self.adjacente(v):
                            if not marcados[z[0]]:
                                marcados[z[0]] = True
                                antecessores[z[0]] = v
                                vertices.append(z[0])
                    else:
                        for z in self.adjacente(v):
                            if not marcados[z]:
                                marcados[z] = True
                                antecessores[z] = v
                                vertices.append(z)
        return antecessores

    def converterListaMatriz(self):
        return GrafoMatrizes(self.iteravel, self.ponderado, self.direcionado)

import numpy as np

class GrafoMatrizes:
    def __init__(self, iteravel, ponderado=False, direcionado=False):
        self.iteravel = iteravel
        self.ponderado = ponderado
        self.direcionado = direcionado
        self.v = []
        for duplas in self.iteravel:
            if self.ponderado:
                for vertice in duplas[:len(duplas)-1]:
                    if vertice not in self.v:
                        self.v.append(vertice)
            else:
                for vertice in duplas:
                    if vertice not in self.v:
                        self.v.append(vertice)
        self.matrizesDeAdj = self.criarMatrizes(iteravel, ponderado, direcionado)

    def index(self, vertice):
        aux = 0
        for n in range(len(self.v)):
            if self.v[n] != vertice:
                aux += 1
            else:
                return aux
    
    def criarMatrizes(self, iteravel, ponderado, direcionado):
        tam = len(self.v)
        corpo = np.zeros((tam,tam), int)
        if not self.ponderado:
            if not self.direcionado:
                for x in iteravel:
                    corpo[self.index(x[0])][self.index(x[1])] = 1
                    corpo[self.index(x[1])][self.index(x[0])] = 1
            else:
                for x in iteravel:
                    corpo[self.index(x[0])][self.index(x[1])] = 1
        else:
            if not self.direcionado:
                for x in iteravel:
                    corpo[self.index(x[0])][self.index(x[1])] = x[2]
                    corpo[self.index(x[1])][self.index(x[0])] = x[2]
            else:
                for x in iteravel:
                    corpo[self.index(x[0])][self.index(x[1])] = x[2]
        return corpo
        
    def __str__(self):
        tam = max(self.v)
        colunas = str([x for x in self.v])
        colunas = '   ' + colunas[1:len(colunas)-1].replace(',','')
        print(colunas)
        for x in range(len(self.matrizesDeAdj)):
            print(str(self.v[x]) + ' ' + str(self.matrizesDeAdj[x]))

    def __repr__(self):
        return 'GrafoMatrizes(' + str(self.iteravel) + ')'

    def __getItem__(self, index):
        arestas = {}
        if not self.ponderado:
            for x in range(len(self.matrizesDeAdj)):
                if index not in arestas and self.matrizesDeAdj[index][x] != 0:
                    arestas[index] = [(index, x)]
                elif index in arestas and self.matrizesDeAdj[index][x] != 0:
                    arestas[index].append((index, x))
                if self.direcionado:
                    if index not in arestas and self.matrizesDeAdj[x][index] != 0:
                        arestas[index] = [(x, index)]
                    elif index in arestas and self.matrizesDeAdj[x][index] != 0:
                        arestas[index].append((x, index))
        else:
            for x in range(len(self.matrizesDeAdj)):
                if index not in arestas and self.matrizesDeAdj[index][x] != 0:
                    arestas[index] = [(index, x, self.matrizesDeAdj[index][x])]
                elif index in arestas and self.matrizesDeAdj[index][x] != 0:
                    arestas[index].append((index, x, self.matrizesDeAdj[index][x]))
                if self.direcionado:
                    if index not in arestas and self.matrizesDeAdj[x][index] != 0:
                        arestas[index] = [(x, index, self.matrizesDeAdj[index][x])]
                    elif index in arestas and self.matrizesDeAdj[x][index] != 0:
                        arestas[index].append((x, index, self.matrizesDeAdj[index][x]))
        return arestas[index]

    def grauDeSaida(self, vertice):
        if vertice not in self.v:
            return '[' + str(vertice) + '] não encontrado.'
        aux = 0
        for n in range(len(self.v)):
            if self.matrizesDeAdj[self.index(vertice)][n] != 0:
                aux += 1
        return aux

    def grauDeEntrada(self, vertice):
        if not self.direcionado:
            return self.grauDeSaida(vertice)
        else:
            aux = 0
            for n in range(len(self.v)):
                if self.matrizesDeAdj[n][self.index(vertice)] != 0:
                    aux += 1
            return aux

    def ligados(self, tupla):
        if type(tupla) is int:
            return '[' + str(tupla) + '] não encontrado. Formato inválido.'
        elif len(tupla) != 2:
            return '[' + str(tupla) + '] não encontrado. Formato inválido.'
        elif tupla[0] not in self.v or tupla[1] not in self.v:
            return '[' + str(tupla) + '] não encontrado. Par não existente nessa tupla.'
        if self.matrizesDeAdj[self.index(tupla[0])][self.index(tupla[1])] or self.matrizesDeAdj[self.index(tupla[1])][self.index(tupla[0])] != 0:
            return True
        return False

    def adjacente(self, vertice):
        if vertice not in self.v:
            return '[' + str(vertice) + '] não encontrado.'
        else:
            lista = []
            for x in self.v:
                if not self.direcionado:
                    if self.matrizesDeAdj[self.index(vertice)][self.index(x)] != 0:
                        lista.append(x)
                else:
                    if self.matrizesDeAdj[self.index(vertice)][self.index(x)] != 0:
                        lista.append(x)
                    if self.matrizesDeAdj[self.index(x)][self.index(vertice)] != 0 and x not in lista:
                        lista.append(x)
        return lista

    def maiorAresta(self):
        if not self.ponderado:
            return 'Grafo não-ponderado.'
        maiores = []
        lista = []
        for x in self.matrizesDeAdj:
            maiores.append(max(x))
        maior = max(maiores)
        for n in self.v:
            for m in self.v:
                if self.matrizesDeAdj[self.index(n)][self.index(m)] == maior and (m,n) not in lista:
                    lista.append((n, m))
        return 'Arestas de peso: ' + str(maior) + ' // ' + 'Vértices ligados a ela: ' + str(lista)

    def menorAresta(self):
        if not self.ponderado:
            return 'Grafo não-ponderado.'
        pesos = []
        lista = []
        for x in self.matrizesDeAdj:
            for y in x:
                if y != 0:
                    pesos.append(y)
        menor = min(pesos)
        for n in self.v:
            for m in self.v:
                if self.matrizesDeAdj[self.index(n)][self.index(m)] == menor and (m,n) not in lista:
                    lista.append((n, m))
        return 'Arestas de peso: ' + str(menor) + ' // ' + 'Vértices ligados a ela: ' + str(lista)

    def removeAresta(self, tupla):
        if type(tupla) is int:
            return '[' + str(tupla) + '] não encontrado. Formato inválido.'
        elif len(tupla) != 2:
            return '[' + str(tupla) + '] não encontrado. Formato inválido.'
        elif tupla[0] not in self.v or tupla[1] not in self.v:
            return '[' + str(tupla) + '] não removido. Par não existente nessa tupla.'
        if not self.direcionado:
            self.matrizesDeAdj[self.index(tupla[0])][self.index(tupla[1])] = 0
            self.matrizesDeAdj[self.index(tupla[1])][self.index(tupla[0])] = 0
        else:
            self.matrizesDeAdj[self.index(tupla[0])][self.index(tupla[1])] = 0
        print('[' + str(tupla) + '] removida.')

    def adicionaAresta(self, tupla):
        if type(tupla) is int:
            return '[' + str(tupla) + '] não encontrado. Formato inválido.'
        elif not self.ponderado and len(tupla) != 2:
            return '[' + str(tupla) + '] não encontrado. Formato inválido.'
        elif self.ponderado and len(tupla) != 3:
            return '[' + str(tupla) + '] não encontrado. Formato inválido.'
        elif tupla[0] not in self.v or tupla[1] not in self.v:
            return '[' + str(tupla) + '] não adicionado. Par não existente nessa tupla.'
        if not self.ponderado:
            if not self.direcionado:
                self.matrizesDeAdj[self.index(tupla[0])][self.index(tupla[1])] = 1
                self.matrizesDeAdj[self.index(tupla[1])][self.index(tupla[0])] = 1
            else:
                self.matrizesDeAdj[self.index(tupla[0])][self.index(tupla[1])] = 1
            self.iteravel
        else:
            if not self.direcionado:
                self.matrizesDeAdj[self.index(tupla[0])][self.index(tupla[1])] = tupla[2]
                self.matrizesDeAdj[self.index(tupla[1])][self.index(tupla[0])] = tupla[2]
            else:
                self.matrizesDeAdj[self.index(tupla[0])][self.index(tupla[1])] = tupla[2]
        if type(self.iteravel[0]) is tuple:
            self.iteravel += tuple(tupla),
        elif type(self.iteravel[0]) is list:
            self.iteravel.append(list(tupla))
        print('[' + str(tupla) + '] adicionada.')

    def adicionaVertice(self, vertice):
        if vertice in self.v:
            return '[' + str(vertice) + '] já existente.'
        self.v.append(vertice)
        self.matrizesDeAdj = self.criarMatrizes(self.iteravel, self.ponderado, self.direcionado)
        print('[' + str(vertice) + '] adicionado.')

    def dfs(self, vertice, antecessor, marcado):
        marcado[self.index(vertice)] = True
        for u in self.adjacente(vertice):
            if not marcado[self.index(u)]:
                antecessor[self.index(u)] = vertice
                self.dfs(u, antecessor, marcado)

    def buscaEmProfundidade(self):
        marcado = len(self.v) * [False]
        antecessor = len(self.v) * [-1]
        for vertice in self.v:
            if not marcado[self.index(vertice)]:
                self.dfs(vertice, antecessor, marcado)
        for i in range(0, len(self.v)):
            print(str(i) + ': ' + str(antecessor[i]))

    def buscaEmLargura(self):
        marcado = len(self.v) * [False]
        antecessor = len(self.v) * [-1]
        vertices = []
        for i in self.v:
            if not marcado[self.index(i)]:
                vertices.append(i)
                marcado[self.index(i)] = True
                while len(vertices) > 0:
                    v = vertices.pop(0)
                    for u in self.adjacente(v):
                        if not marcado[self.index(u)]:
                            marcado[self.index(u)] = True
                            antecessor[self.index(u)] = v
                            vertices.append(u)
        for i in range(0, len(self.v)):
            print(str(i) + ': ' + str(antecessor[i]))

    def converterMatrizLista(self):
        return GrafoLista(self.iteravel, self.ponderado, self.direcionado)