# Criando a lista numeros 
numeros = []

for contador in range(0,5):
    valor = float(input("Insira um numero: ")) 
    numeros.append(valor)

print ("Lista de numeros digitados : ",numeros)
#inverter os elementos da lista
numeros.reverse()
print ("Lista invertida            : ",numeros)

