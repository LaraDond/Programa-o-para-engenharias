#ler nome, altura e peso + ordem alfabética

dic = {}
lista_peso = []

for i in range (3):
    nome = input("Dgite o nome: ")
    altura = float(input("Digite a altura: "))
    peso = float(input("Digite o peso: "))
    print("************************")

    lista = []
    lista.append(altura)
    lista.append(peso)

    lista_peso.append(peso)

    dic.update({nome:lista})

print("A lista de nome, altura e peso é: ", dic)
print("A menor altura é: ", min(dic, key=dic.get) )
print("O peso médio do grupo é: ", (sum(lista_peso))/3) 
print("Lista em ordem alfabética: ", sorted(dic.items())) 
  

