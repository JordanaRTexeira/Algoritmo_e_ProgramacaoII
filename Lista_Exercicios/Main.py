from Torre import Torre
from Apartamento import Apartamento

print (" --- Dados Torre --- ")
blocoA = Torre()
blocoA.cadastrar()
blocoA.imprimir()

print (" --- Dados Apartamento---")
ap03 = Apartamento()
ap03.cadastrarApartamento(blocoA)
ap03.imprimirApartamento()



