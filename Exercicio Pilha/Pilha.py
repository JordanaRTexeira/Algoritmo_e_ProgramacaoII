from No import No

class Pilha: 
    def __init__(self):
        self.primeiro = None
        self.tamanho = 0

    def vazia(self):
        if self.tamanho == 0:
            return True
        return False

    def adicionar(self, valor):
        no = No(valor)
        if self.vazia():
            self.primeiro = no
        else:
            aux = self.primeiro
            self.primeiro = no
            no.proximo = aux
        self.tamanho += 1

    def imprimir(self):
        if self.vazia():
            print('--- Pilha Vazia ---')
        else:
            aux = self.primeiro
            while(aux):
                print(str(aux.item))
                aux = aux.proximo
                
                
    def remover(self):
        if self.vazia():
            print('--- Pilha Vazia ---')
        else:
            aux = self.primeiro.proximo
            self.primeiro = aux
            self.tamanho -= 1
        
    def __len__(self):
        if self.vazia():
            print('--- Pilha Vazia ---')
        else:
            print('Pilha(s) contém {} itens'.format(str(self.tamanho)))