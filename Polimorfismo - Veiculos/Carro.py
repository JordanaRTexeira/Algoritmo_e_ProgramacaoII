from Automovel import Automovel

class Carro(Automovel):
    def __init__(self, marca, qtdRodas, modelo, potenciaMotor, qtdPortas, velocidade = 0):
        Automovel.__init__(self, marca, qtdRodas, modelo, velocidade, potenciaMotor)
        self.qtdPortas = qtdPortas

    def imprimirinformacoes(self):
        print(" -Veículo de marca:", self.marca, " \n -Modelo:", self.modelo,
              " \n -Quantidade de rodas:", self.qtdRodas, 
              " \n -Potência do motor: ", self.potenciaMotor," \n -Quantidade de portas: ", self.qtdPortas,
              " \n -Velocidade: ", self.velocidade)
