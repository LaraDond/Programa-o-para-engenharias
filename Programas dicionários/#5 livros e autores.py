#5 livros e autores

dicionario = {}

for i in range (5):
    livro = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    print("***********************************")

    dicionario[livro] = autor

print("As informações registradas foram: ",dicionario)
