#criar um dicionario vazio
mercado  = {}

while True:
    nome     = input("Digite nome produto : ")
    preco    = float(input("Digite preço R$ : "))  
    #incluir elemento no dicionario 
    mercado[nome] = preco
    opcao = input("Deseja continuar S ou N ? ").upper()
    if opcao == "N":
        break
  
print ("Lista de produtos mercardo : ", mercado)

novonome  = input("Qual nome produto deseja incluir ? ")
novopreco = float(input("Qual preço deseja incluir ? "))
#incluir novo elemento do dicionario
mercado.update({novonome:novopreco})

print ("Lista de produtos atualizada: ", mercado)

