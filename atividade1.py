lista_precos_produtos = ['5.20', '8', '2.49']
lista_quantidade =['3', '5', '10']
lista_produtos = ['SHAMPOO', 'CONDICIONADOR', 'SABONETE']


def cadastrar_produto():
    while True:
        print("--- Cadastro ---")
        lista_produtos.append(ler_produto("Nome do produto: "))
        lista_precos_produtos.append(ler_produto("Preço do produto: "))
        lista_quantidade.append(ler_produto("Digite quantidade de produto(s): "))
        input("------ Produto Cadastrado ! [Enter]")
        op = input( "Deseja continuar? [s/n]" ).lower()
        if op == 'n' :
            break
        else :
            continue
def ler_produto(mensagem):
    return input(mensagem).upper()

def imprimir():
    print("Produto(s): ", lista_produtos)
    print("Preço(s): ", lista_precos_produtos)
    print("Quantidade(s): ", lista_quantidade)

def produto_valido(mensagem):
    while True:
        produto = ler_produto(mensagem)
        if produto in lista_produtos:
            return produto
        input("Erro! Produto não encontrado. [Enter]")

def relatorio_por_produto():
    print("Produto(s): ", lista_produtos)
    produto_escolhida = produto_valido("Digite um produto: ")
    print("---Relatório por produto---")
    for ind, produto in enumerate(lista_produtos):
        if produto == produto_escolhida:
            print("\t- Produto selecionado: ", lista_produtos[ind])
            print("\t- Preço do produto:", lista_precos_produtos[ind])
            print("\t- Quantidade: ", lista_quantidade[ind])
    input("[Enter]")

def removeritem():
    print("----- Produtos existentes:")
    for produto in lista_produtos:
        print("  > ", produto)
    produto_a_excluir = produto_valido("Digite o produto que deseja excluir :")
    for ind, produto in enumerate(lista_produtos):
        if produto == produto_a_excluir:
            lista_produtos.pop(ind)
            lista_precos_produtos.pop(ind)
            lista_quantidade.pop(ind)
    input("----- Produto excluído com sucesso. [Enter]")

def menu():
    while True:
        escolha = input(''' 
        MENU
        |-----------------------------------------------|                    
        |1- Cadastrar Produtos (Preços e quantidade)    |
        |2- Imprimir lista(s)                           |
        |3- Escolha um produto e exclua da lista        |
        |4- Relatório por produto                       |
        |-----------------------------------------------|
           Sua escolha: '''
                    )
        if escolha == '0': break
        elif escolha == '1': cadastrar_produto()
        elif escolha == '2': imprimir()
        elif escolha == '3': removeritem()
        elif escolha == '4': relatorio_por_produto()
        else: input("ERRO! escolha um número conforme o menu. [ENTER] continua.")

#### Programa Principal.
menu()


