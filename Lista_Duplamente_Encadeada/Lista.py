from No import No

class Lista:
    def __init__(self):
        self.inicio= None
        self.fim = None
        self.tamanho = 0
   
    def __len__(self):
        return self.tamanho

    def adicionar(self, valor):
        if self.inicio: 
            aux = self.inicio
            anterior = None
            while(aux.proximo):
                anterior = aux
                aux = aux.proximo
            aux.proximo = No(valor)
            aux.proximo.anterior = aux
            aux.anterior = anterior
            if self.fim:
                self.fim = aux.proximo
        else:
            self.inicio = No(valor)
            self.fim = No(valor)
        self.tamanho += 1


    def imprimir_ListaOrdenada(self):
        if self.inicio == None:
            print("Lista Vazia !!")

        aux = self.inicio
        while(aux):
            print(aux.dado)
            aux = aux.proximo
        print("- Tamanho da lista: " + str(self.tamanho))
        print("\n ---------------------------\n")
    
    def imprimir_ListaOrdemInversa(self):
        aux = self.fim
        print("--- Lista em ordem inversa ---")
        while(aux):
            print(aux.dado)
            aux = aux.anterior
        print("- Tamanho da lista: " + str(self.tamanho))
        print("\n ---------------------------\n")
