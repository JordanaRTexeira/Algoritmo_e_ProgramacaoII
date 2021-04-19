from Pessoa import Pessoa

class Juridica(Pessoa):
    def __init__(self, __codigo, nome, _endereco, __telefone, __cnpj, __inscricaoEstadual, quantidadeFuncionarios):
        Pessoa.__init__(self, __codigo, nome, _endereco, __telefone)
        self.__cnpj              = __cnpj
        self.__inscricaoEstadual = __inscricaoEstadual
        self.quantidadeFuncionarios     = quantidadeFuncionarios

    def imprimirCNPJ(self):
        print("A empresa ",self.nome, "possui CNPJ: ",self.__cnpj)

    def __emitirNotaFiscal(self):
        print("Nota fiscal de " ,self.nome,"para a empresa de CNPJ: ",self.__cnpj)