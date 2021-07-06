from Pilha import Pilha
from Livro import Livro
from Autor import Autor


autorId = input("Digite a ID do Autor : ")
autorNome = input("Digite o Nome do Autor : ")
print ("---- DADOS DO AUTOR ----")
autor = Autor(autorId, autorNome)
autor.imprimir()

livroId = input("Digite a ID do Autor : ")
livroTitulo = input("Digite o título do livro : ")
livroAutor = autor.nome_publico
livro = Livro(livroId, livroTitulo, livroAutor)

print(f"Livro: {livro.id}, Título do Livro: {livro.titulo}, Autor do Livro: {livro.autor}") 

livroId2 = input("Digite a ID do Autor : ")
livroTitulo2 = input("Digite o título do livro : ")
livroAutor2 = autor.nome_publico
livro2 = Livro(livroId2, livroTitulo2, livroAutor2)
print(f"Livro : {livro2.id}, Título do Livro: {livro2.titulo}, Autor do Livro: {livro2.autor}")

pilha = Pilha()
print("---- LIVROS ----")
pilha.adicionar(livro.titulo)
pilha.adicionar(livro2.titulo)
print(pilha)
print("----- REMOVENDO UM LIVRO DA PILHA ----")
pilha.remover()
print(pilha)

