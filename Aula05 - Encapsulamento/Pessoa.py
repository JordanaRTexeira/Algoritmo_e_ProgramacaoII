class Pessoa():
    
    def __init__(self, _codigo, nome, __endereco, _telefone):
        self._codigo = _codigo
        self.nome = nome
        self.__endereco = __endereco
        self._telefone = _telefone
    
    def imprimirNome(self):
        print("Nome: ", self.nome)
    
    def __imprimirTelefone(self):
        print("Telefone: ", self._telefone)