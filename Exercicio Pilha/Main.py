from Pilha import Pilha

pilha = Pilha()
menu = '''
*--------MENU-------*
|                   |
|  1 - Adicionar    |
|  2 - Imprimir     |
|  3 - Remover      |
|  4 - Tamanho      |
|  5 - Sair         |
*-------------------*
- Escolha uma opção:  '''

while True:
    op = (input(menu))

    if op == '1':
       pilha.adicionar(input('Insira um valor: '))
    elif op == '2':
       pilha.imprimir()   
    elif op == '3':
       pilha.remover()
    elif op == '4':
       pilha.__len__()   
    elif op == '5':
        break
    else:
        print('Opção inválida. Tente novamente.')