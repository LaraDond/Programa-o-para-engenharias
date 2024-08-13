#nomes e telefones

dicionario = {}

for i in range(10):
    nome = input("Digite o nome do seu amigo: ")
    telefone = int(input("Digite o telefone do seu amigo: "))
    print("************************************")

    dicionario[nome] = telefone

print("As informações passadas foram: ",dicionario)

    
