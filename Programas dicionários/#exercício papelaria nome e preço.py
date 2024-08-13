#exercício papelaria nome e preço

produtos = {}
n = int(input("Quantos produtos deseja cadastrar? "))

for i in range(n):
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o valor do produto: "))

    #adicionar no diionário
    produtos.update({nome:preco})
    
print("A lista de produtos é: ",produtos)

remover = input("Qual produto deseja excluir: ")

produtos.pop(remover)

print("Lista de produtos atualizada: ",produtos)

