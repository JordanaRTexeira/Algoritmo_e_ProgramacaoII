from Veiculo import Veiculo

class Automovel(Veiculo):
    potenciaMotor: float

    def __init__(self, marcaV, qtdRodasV, modeloV, potenciaMotor,velocidadeV = 0):
        Veiculo.__init__(self, marcaV, qtdRodasV, modeloV, velocidadeV)
        self.potenciaMotor = potenciaMotor

    def imprimirinformacoes(self):
        print(" -Veículo de marca: ", self.marca,  " \n -Modelo: ", self.modelo, "\n -Quantidade de Rodas: ", self.qtdRodas, 
              "\n -Potência Motor: ", self.potenciaMotor, "\n -Velocidade: ", self.velocidade)
