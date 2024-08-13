#Questão 2

print("Para sair digite 'SAIR'.")

lista = []

while True:
    nome = input("Digite um nome: ")

    if nome.upper() == "SAIR":
        print("Fim de lista.")
        break
    
    else:
        lista.append(nome)

lista.sort(reverse = False)

print("A lista de nomes, em ordem alfabética é: ",lista)

        
        
