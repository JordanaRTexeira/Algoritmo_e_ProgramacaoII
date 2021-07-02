class Apartamento:
    def __init__(self):
        self.id = int()
        self.numero = str()
        self.torre = None
        self.vaga = int()
        self.proximo = None

    def cadastrarApartamento(self, valor):
        self.id = (input("Insira o ID do Apartamento: "))
        self.numero = (input("Insira o Número do Apartamento: "))
        self.torre = valor

    def imprimirApartamento(self):
        print(f"O ID do Apartamento é {self.id} no número {self.numero} localizado na Torre {self.torre.nome}")

