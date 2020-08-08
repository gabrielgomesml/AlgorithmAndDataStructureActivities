class No:
    def __init__(self, chave=None, valor=None, esquerda=None, direita=None, pai=None):
        self.chave = chave
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita
        self.pai = pai
        self.altura = 0

    def __it__(no1, no2):
        if type(no1) != type(no2):
            raise TypeError
        else:
            if no1.valor < no2.valor:
                return True
            return False

    def __gt__(no1, no2):
        if type(no1) != type(no2):
            raise TypeError
        else:
            if no1.valor > no2.valor:
                return True
            return False

    def __le__(no1, no2):
        if type(no1) != type(no2):
            raise TypeError
        else:
            if no1.valor <= no2.valor:
                return True
            return False

    def __ge__(no1, no2):
        if type(no1) != type(no2):
            raise TypeError
        else:
            if no1.valor >= no2.valor:
                return True
            return False

    def __eq__(no1, no2):
        if type(no1) != type(no2):
            raise TypeError
        else:
            if no1.valor == no2.valor:
                return True
            return False

    def __ne__(no1, no2):
        if type(no1) != type(no2):
            raise TypeError
        else:
            if no1.valor != no2.valor:
                return True
            return False
        

class ArvoreBinaria:
    def __init__(self):
        self.raiz = No(None, None)

    def __bool__(self):
        if self.raiz.chave == None:
            return False
        return True

    def inserir(self, chave, valor=None):
        novoNo = No(chave, valor)
        if self.raiz.chave == None:
            self.raiz = novoNo
        else:
            arvore = self.raiz
            while True:
                if novoNo.chave < arvore.chave:
                    if not arvore.esquerda:
                        arvore.esquerda = novoNo
                        arvore.esquerda.pai = arvore
                        return
                    arvore = arvore.esquerda
                elif novoNo.chave > arvore.chave:
                    if not arvore.direita:
                        arvore.direita = novoNo
                        arvore.direita.pai = arvore
                        return
                    arvore = arvore.direita
                else:
                    print('Chave [' + str(chave) + '] já está na árvore.')
                    return

    def emPreOrdem(self, arvore):
        if not arvore:
            return ''
        else:
            return str(arvore.valor) + ', ' + self.emPreOrdem(arvore.esquerda) + self.emPreOrdem(arvore.direita)

    def emOrdem(self, arvore):
        if not arvore:
            return ''
        else:
            return self.emOrdem(arvore.esquerda) + str(arvore.valor) + ', ' + self.emOrdem(arvore.direita)
        
    def getChaves(self, arvore):
        if not arvore:
            return ''
        else:
            return self.getChaves(arvore.esquerda) + str(arvore.chave) + ', ' + self.getChaves(arvore.direita)

    def __str__(self):
        string = self.emOrdem(self.raiz)
        return string[:len(string) - 2]
        
    def __repr__(self):
        string = self.emPreOrdem(self.raiz)
        return 'ArvoreBinaria([' + string[:len(string) - 2] + '])'

    def adicionaNos(self, arvore):
        if not arvore:
            return []
        else:
            return [arvore] + self.adicionaNos(arvore.esquerda) + self.adicionaNos(arvore.direita)
        
    def __iter__(self):
        self.pilha = self.adicionaNos(self.raiz)
        return self

    def __next__(self):
        if len(self.pilha) == 0:
            raise StopIteration
        item = self.pilha.pop(0)
        item = item.valor
        return item

    def minimo(self, raiz):
        while raiz.esquerda:
            raiz = raiz.esquerda
        return raiz

    def maximo(self, raiz):
        while raiz.direita:
            raiz = raiz.direita
        return arvore

    def sucessor(self, raiz):
        if raiz.direita:
            return self.minimo(raiz.direita)
        novoPai = raiz.pai
        while novoPai and raiz is novoPai.direita:
            raiz = novoPai
            novoPai = novoPai.pai
        return novoPai.chave

    def antecessor(self, raiz):
        if raiz.esquerda:
            return self.minimo(raiz.esquerda)
        novoPai = raiz.pai
        while novoPai and raiz is novoPai.esquerda:
            raiz = novoPai
            novoPai = novoPai.pai
        return novoPai.chave

    def transplante(self, no1, no2):
        if not no1.pai:
            self.raiz = no2
        elif no1 is no1.pai.esquerda:
            no1.pai.esquerda = no2
        else:
            no1.pai.direita = no2
        if no2:
            no2.pai = no1.pai

    def __getNo__(self, chave):
        arvore = self.raiz
        if not arvore.chave:
            print('A árvore está vazia.')
            return False
        while arvore:
            if arvore.chave == chave:
                return arvore
            elif chave < arvore.chave:
                arvore = arvore.esquerda
            else:
                arvore = arvore.direita
        print('Chave [' + str(chave) + '] não está presente está na árvore.')
        return False

    def __delitem__(self, chave):
        arvore = self.__getNo__(chave)
        if arvore is False:
            return
        if not arvore.esquerda:
            self.transplante(arvore, arvore.direita)
        elif not arvore.direita:
            self.transplante(arvore, arvore.esquerda)
        else:
            y = self.minimo(arvore.direita)
            if y.pai != arvore:
                self.transplante(y, y.direita)
                y.direita = arvore.direita
                y.direita.pai = y
            self.transplante(arvore, y)
            y.esquerda = arvore.esquerda
            y.esquerda.pai = y
        return 'Chave [' + str(chave) + '] removida.'

    def __contais__(self, chave):
        arvore = self.__getNo__(chave)
        if not arvore:
            return False
        else:
            return True

    def valores(self):
        return self.__str__()

    def chaves(self):
        arvore = self.getChaves(self.raiz)
        return arvore[:len(arvore) - 2]
        
    def __getValor__(self, chave):
        arvore = self.raiz
        if not arvore.chave:
            print('A árvore está vazia.')
            return False
        while arvore:
            if arvore.chave == chave:
                return arvore.valor
            elif chave < arvore.chave:
                arvore = arvore.esquerda
            else:
                arvore = arvore.direita
        print('Chave [' + str(chave) + '] não está presente está na árvore.')
        return False

    def __setValor__(self, chave, valor):
        arvore = self.raiz
        if not arvore.chave:
            print('A árvore está vazia.')
            return False
        while arvore:
            if arvore.chave == chave:
                arvore.valor = valor
                return 
            elif chave < arvore.chave:
                arvore = arvore.esquerda
            else:
                arvore = arvore.direita
        print('Chave [' + str(chave) + '] não está presente está na árvore.')
        return False