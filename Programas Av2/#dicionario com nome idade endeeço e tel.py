#dicionario com nome idade endeeço e telefone 

d = {}

for i in range (3):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    endereco = input("Digite o endereço: ")
    telefone = int(input("Digite o telefone: "))
    print("************************")

    lista = []
    lista.append(idade)
    lista.append(endereco)
    lista.append(telefone)

    d.update({nome:lista})

print("O dicionário final é: ", d)    