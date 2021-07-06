class Autor:
    __id = str()

    def __init__(self, id, nome_publico):
        self.__id = id
        self.nome_publico = str(nome_publico)
    
    def imprimir(self):
        print("ID: ", self.__id)
        print("Nome do Autor: ", self.nome_publico)


    