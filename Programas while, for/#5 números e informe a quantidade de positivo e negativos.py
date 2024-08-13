#5 números e informe a quantidade de positivo e negativos

positivo = 0
negativo = 0

for contador in range (0,5):
    numero = int(input("Digite um número: "))

    if (numero > 0):
        positivo = positivo + 1
    
    if (numero < 0):
        negativo = negativo + 1

print("Quantidade números positivos: ",positivo)
print("Quantidade números negativos: ",negativo)

        
        
