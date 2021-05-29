from Lista import Lista

lista = Lista()
lista.adicionar(7)
lista.adicionar(13)
lista.adicionar(20)
print("--- Lista em ordem ---- ")
lista.imprimir_ListaOrdenada()
lista.imprimir_ListaOrdemInversa()

valor = input("- Insira um valor: ")
lista.adicionar(valor)
print("\n ---------------------------\n")
print("--- Lista em ordem --- ")
lista.imprimir_ListaOrdenada()
lista.imprimir_ListaOrdemInversa()
