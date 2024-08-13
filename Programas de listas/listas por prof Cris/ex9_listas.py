# Criando a lista numeros 
numeros = []

for contador in range(0,5):
    valor = int(input("Insira um numero: "))
    numeros.append(valor)

print ("Lista de numeros digitados : ",numeros)
print ("Maior valor lista : ",max(numeros))
print ("Menor valor lista : ",min(numeros))
