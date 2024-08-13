#idade e organizar de menor para maior 

lista = []

for i in range (10):
    idade = int(input("Digite sua idade: "))
    lista.append(idade)

lista.sort(reverse = False)

print("A lista de idades em ordem crescente é: ", lista)
