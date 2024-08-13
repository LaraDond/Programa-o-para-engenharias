# Criando a lista amigos 
amigos = []

while True: 
    nome = input("Insira um nome de amigo: ") 
    amigos.append(nome)
    opcao = input("Deseja continuar cadastro? S ou N  ").upper()
    if opcao == "N":
        break

print ("lista de amigos ",amigos)
