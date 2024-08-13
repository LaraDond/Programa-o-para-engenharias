# Criando a lista
numeros = []

for contador in range(5):
    valor = int(input("Digite um valor: "))
    numeros.append(valor)

print ("lista de numeros     : ", numeros)
print ("soma elementos lista : ", sum(numeros))


