from Pessoa import Pessoa

class Fisica(Pessoa):
    altura: float
    peso: float
    idade: int    
            
    def __init__(self, __codigo, nome, _endereco, __telefone, __cpf, idade, peso, altura):
        Pessoa.__init__(self, __codigo, nome, _endereco, __telefone)
        self.__cpf = __cpf
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def imprimirCPF(self):
        print ("-Nome: ", self.nome, "\n-CPF: ",self.__cpf)
    
    def __calcularIMC(self):
        imc = self.peso / (self.altura * 2)
        print("-Peso: ", self.peso, "\n-Altura: ", self.altura, "\n-Seu IMC é: ",imc)
    