#10 numeros e leia maior e menor

numero = int(input("Digite o primeiro número: "))

maior = numero
menor = numero

for contador in range (0,9):
    numero = int(input("Digite outro número: "))

    if (numero > maior):
        maior = numero

    if (numero < menor):
        menor = numero

print("O maior número é: ", maior)
print("O menor número é: ", menor)
        

        
                 
    
