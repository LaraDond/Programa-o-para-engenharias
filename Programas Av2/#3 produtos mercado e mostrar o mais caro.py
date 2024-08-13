#3 produtos mercado e mostrar o mais caro 

dic = {}

for i in range(3):
    nome = input("Digite o nome do produto: ")
    valor = float(input("Digite o preço do produto: "))
    print("******************")

    dic.update({nome:valor})

produto_mais_caro = max(dic, key=dic.get)

print("A lista é: ",dic)
print("Mais caro: ", produto_mais_caro)




