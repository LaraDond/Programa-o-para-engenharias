#nome e telefone 5 amigos e depois inserir mais um

agenda = {}

for i in range(5):
    nome = input("Digite o nome do seu amigo: ")
    telefone = int(input("Digite o telefone: "))
    print("*********************")

    agenda [nome] = telefone

print("Lista de contatos: ",agenda)

novonome = input("Qual nome deseja incluir? ")
novotelefone = int(input("Qual telefone deseja incluir? "))

agenda.update({novonome:novotelefone})

print("Lista atualiada: ", agenda)


                 
