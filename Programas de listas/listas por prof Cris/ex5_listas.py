# Criando as listas
numeros = []
pares   = []
impares = []

for contador in range(0,10):
    valor = int(input("Digite um numero inteiro: "))
    numeros.append(valor)
    if (valor % 2) == 0 :
           pares.append(valor)
    else :
           impares.append(valor)

print ("lista de numeros : ", numeros )
print ("Lista pares      : ", pares)
print ("Lista impares    : ", impares)

