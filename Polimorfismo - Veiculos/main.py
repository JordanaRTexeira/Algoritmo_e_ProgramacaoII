from Veiculo import Veiculo
from Automovel import Automovel
from Carro import Carro
from Moto import Moto
from Bicicleta import Bicicleta

print("--- CLASSE VEÍCULO ---")
veiculo1 = Veiculo("Fiat", 4 , "Palio")
veiculo1.imprimirinformacoes()
print(" -Velocidade (Função Acelerar): ", veiculo1.acelerar(100))
print(" -Velocidade (Função Frear): ", veiculo1.frear(100))


###########################################################
print ("--- CLASSE AUTOMÓVEL ---")
automovel1 = Automovel("Honda", 4, "Civic", 1.6, 20)
automovel1.imprimirinformacoes()

###########################################################
print ("--- CLASSE CARRO ---")
carro1 = Carro("Jeep", 4, "Renegade", 0 , 4, 2.0)
carro1.imprimirinformacoes()

###########################################################
print ("--- CLASSE MOTO ---")
moto1 = Moto("Yamaha", "Fazer",2, 0, True,250)
moto1.imprimirinformacoes()

###########################################################
print ("--- CLASSE BICICLETA ---")
bicicleta1 = Bicicleta("Caloi", 2, "Elétrica", 6, False, 10)
bicicleta1.imprimirinformacoes()

