#leia 5 números e calcule média, com repetição

soma = 0
for contador in range(1,6):
    numeros = float(input("Digite um número: "))

    soma = soma + numeros
    
print("A média é: ", soma/contador)
