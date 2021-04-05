from Automovel import Automovel

class Moto(Automovel):
    partidaEletrica: bool

    def __init__(self, marca, qtdRodas, modelo, potenciaMotor, partidaEletrica, velocidade = 0):
        Automovel.__init__(self, marca, qtdRodas, modelo, velocidade, potenciaMotor)
        self.partidaEletrica = partidaEletrica

    def imprimirinformacoes(self):
        print(" -Veículo de marca:", self.marca, " \n -Modelo:", self.modelo, 
              " \n -Quantidade de rodas:", self.qtdRodas," \n -Potencia do motor: ", self.potenciaMotor,
              " \n -Partida elétrica: ", self.partidaEletrica,
              " \n -Velocidade: ", self.velocidade)
              