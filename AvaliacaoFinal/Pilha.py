from No import No

class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0
    
    def adicionar(self, titulo):
        no = No(titulo)
        no.proximo = self.topo
        self.topo = no
        self.tamanho += 1

    def remover(self):
        if self.tamanho > 0:
            no = self.topo
            self.topo = self.topo.proximo
            self.tamanho -= 1
            return no.dado
        print("Pilha de livros está vazia")

    def verificar(self):
        if self.tamanho > 0:
            return self.topo.dado
        print("A pilha está vazia")

    def __len__(self):
        return self.tamanho
        
    def __repr__(self):
        r = ""
        ponteiro = self.topo
        while ponteiro:
            r = r + str(ponteiro.dado) + "\n"
            ponteiro = ponteiro.proximo
        return r

    def __str__(self):
        return self.__repr__()

    

    