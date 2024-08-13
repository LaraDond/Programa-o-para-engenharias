#lista e medias dos alunos 

lista = []

while True:
    media = float(input("Digite a média do aluno: "))
    lista.append(media)
    continuar = input("Deseja continuar? (S/N)")

    if (continuar.upper()) == "N":
        print ("Fim da lista.")
        break

print("A lista de médias é: ", lista)