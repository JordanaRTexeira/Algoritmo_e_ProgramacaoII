class Veiculo():

    def __init__(self, marca, qtdRodas, modelo, velocidade = 0):
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = velocidade

    def imprimirinformacoes(self):
        print(" -Veículo de marca: ", self.marca, "\n -Modelo: ", self.modelo,  
              "\n -Quantidade de Rodas: ", self.qtdRodas, "\n -Velocidade: ", self.velocidade)
       
    def acelerar(self, valor):
        self.velocidade += valor
        return self.velocidade

    def frear(self, valor):
        self.velocidade -= valor
        return self.velocidade
        
