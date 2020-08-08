class No:
    def __init__(self, item=None, ante=None, prox=None):
        self.item = item
        self.ante = ante
        self.prox = prox

class ListaDupla:
    def __init__(self, initObjeto, contador = 0):
        self.cabeca = self.rabo = None
        self.objeto = initObjeto
        self.contador = contador
        if self.objeto != None:
            for x in self.objeto:
                self.anexar(x)

    def __str__(self):
        elemento = self.cabeca
        string = ''
        while elemento != None:
            string += str(elemento.item) + ','
            elemento = elemento.prox
        return string[:len(string) - 1]

    def __repr__(self):
        return 'ListaDupla([' + self.__str__() + '])'

    def __getitem__(self, indice):
        cont = 0
        elemento = self.cabeca
        while elemento != None:
            if cont == indice:
                return elemento
            else:
                elemento = elemento.prox
                cont += 1
        raise IndexError('list index out of range :( penah')

    def __setitem__(self, indice, novoItem):
        cont = 0
        elemento = self.cabeca
        while elemento != None:
            if cont == indice:
                elemento.item = novoItem
                return
            else:
                elemento = elemento.prox
                cont += 1
        raise IndexError('list index out of range :( penah')

    def indice(self, valor):
        cont = 0
        elemento = self.cabeca
        while elemento != None:
            if valor == elemento.item:
                return cont
            else:
                elemento = elemento.prox
                cont +=1
        raise ValueError('this value can not be found. penah')

    def selecionar(self, indice=None):
        self.indice = indice
        aux = 0
        elemento = self.cabeca
        if self.indice != None and self.indice >= self.contador:
            raise IndexError('list index out of range :( penah')
        elif self.indice == None and self.contador == 0:
            raise IndexError('list index out of range :( penah')
        else:
            if self.contador == 1:
                antigoElemento = self.cabeca
                self.cabeca = self.rabo = None
                self.contador -= 1
                return antigoElemento.item

            elif self.indice == self.contador - 1 or self.indice == None:
                antigoRabo = self.rabo
                novoRabo = self.rabo.ante
                novoRabo.prox = None
                self.rabo = novoRabo
                self.contador -= 1
                return antigoRabo.item

            elif self.indice == 0:
                antigaCabeca = self.cabeca
                novaCabeca = self.cabeca.prox
                novaCabeca.ante = None
                self.cabeca = novaCabeca
                self.contador -= 1
                return antigaCabeca.item
            
            else:
                for x in range(0, self.contador - 1):
                    if self.indice == x:
                        elemento.ante.prox = elemento.prox
                        elemento.prox.ante = elemento.ante
                        self.contador -= 1
                        return elemento.item
                    else:
                        elemento = elemento.prox
                
    def anexar(self, initItem):
        self.item = initItem
        novoNo = No(self.item, None, None)
        if self.rabo == None:
            self.cabeca = novoNo
            self.rabo = novoNo
            self.contador += 1
        else:
            self.rabo.prox = novoNo
            novoNo.ante = self.rabo
            self.rabo = self.rabo.prox
            self.contador += 1

    def concatenar(self, initLista):
        self.lista = initLista
        for x in self.lista:
            self.anexar(x)
        #for x in range(0, len(self.lista) -1):
            #self.lista.selecionar()

class Ponteiro:
    def __init__(self, lista):
        self.indice = lista.cabeca

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice == None:
            raise StopIteration

        item = self.indice.item
        self.indice = self.indice.prox

        return item
            
                
class Fila(ListaDupla):
    def __init__(self, initObjeto, contador = 0):
        self.cabeca = self.rabo = None
        self.objeto = initObjeto
        self.contador = contador
        if self.objeto != None:
            for x in self.objeto:
                self.anexar(x)

    def selecionar(self, indice=None):
        self.indice = indice
        aux = 0
        elemento = self.cabeca
        if self.indice != None and self.indice >= self.contador:
            raise IndexError('list index out of range :( penah')
        elif self.indice == None and self.contador == 0:
            raise IndexError('list index out of range :( penah')
        else:
            if self.contador == 1:
                antigoElemento = self.cabeca
                self.cabeca = self.rabo = None
                self.contador -= 1
                return antigoElemento.item

            elif self.indice == self.contador - 1:
                antigoRabo = self.rabo
                novoRabo = self.rabo.ante
                novoRabo.prox = None
                self.rabo = novoRabo
                self.contador -= 1
                return antigoRabo.item

            elif self.indice == 0  or self.indice == None:
                antigaCabeca = self.cabeca
                novaCabeca = self.cabeca.prox
                novaCabeca.ante = None
                self.cabeca = novaCabeca
                self.contador -= 1
                return antigaCabeca.item
            
            else:
                for x in range(0, self.contador - 1):
                    if self.indice == x:
                        elemento.ante.prox = elemento.prox
                        elemento.prox.ante = elemento.ante
                        self.contador -= 1
                        return elemento.item
                    else:
                        elemento = elemento.prox


class Pilha(ListaDupla):
    def __init__(self, initObjeto, contador = 0):
        self.cabeca = self.rabo = None
        self.objeto = initObjeto
        self.contador = contador
        if self.objeto != None:
            for x in self.objeto:
                self.anexar(x)