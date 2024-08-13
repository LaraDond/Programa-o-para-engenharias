# Criando a lista numeros 
numeros  = []

for contador in range(0,10):
    valor = input("Insira um numero inteiro: ") 
    numeros.append(valor)

print ("lista numeros digitada: ", numeros)
print ("Lista numeros ordem inversa: ", numeros.reverse())
