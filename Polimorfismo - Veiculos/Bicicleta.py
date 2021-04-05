from Veiculo import Veiculo

class Bicicleta(Veiculo):
    numMarchas: int
    bagageiro: bool

    def __init__(self, marca, qtdRodas, modelo, numMarchas, bagageiro, velocidade=0):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro

    def imprimirinformacoes(self):
        print(" -Marca:", self.marca, " \n -Quantidade de rodas:", self.qtdRodas, " \n -Modelo:", self.modelo,
              " \n -Velocidade: ", self.velocidade, " \n -Número de marchas: ", self.numMarchas,
              " \n -Bagageiro: ", self.bagageiro)
   