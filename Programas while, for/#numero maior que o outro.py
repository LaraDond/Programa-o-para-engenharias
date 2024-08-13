#numero maior que o outro

numero = int(input("Digite o 1 número; "))

maior = numero #aqui pode colocar zero
menor = numero #e aqui um número bem grande

for contador in range (1,10):
    
    numero = int(input("Digite um número: "))

    if numero > maior:
        maior = numero

    elif numero < menor:
        menor = numero

print("Maior número digitado: ", maior)
print("Menor número digitado: ", menor)
        
    
                 
