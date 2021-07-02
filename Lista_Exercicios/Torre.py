class Torre:
    def __init__(self):
        self.id = int()
        self.nome = str()
        self.endereco = str()

    def cadastrar(self):
        self.id = int(input("Insira o ID da Torre: "))
        self.nome = str(input("Insira o nome da Torre: "))
        self.endereco = str(input("Insira o endereço da Torre: "))

    def imprimir(self):
        print(f"A ID da Torre é {self.id} e o nome é {self.nome} localizada no endereço {self.endereco}")