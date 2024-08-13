#dicionario com 4 entradas 

dic = {}
valor_compra = []

while True:
    codigo = int(input("Digite o código do produto: "))
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto, em reais: "))
    quantidade = int(input("Digite a quantidade comprada: "))
    print("*******************************")
    continuar = input("Deseja continuar? (S ou N): ").upper()

    lista = []
    lista.append(nome)
    lista.append(preco)
    lista.append(quantidade)

    dic.update({codigo:lista})

    valor = preco*quantidade
    valor_compra.append(valor)

    if continuar == "N":
        break

print("A lista de compras é: ", dic)
print("O valor total das compras, em reais, é: ", sum(valor_compra)) 

