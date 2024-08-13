#2 números e mostre o intervalo entre eles e a soma

n1 = int(input("Digite o primeiro número: "))

n2 = int(input("Digite o segundo número: "))

soma = 0

for contador in range (n1,n2+1):
    print (contador)

    soma += contador

print ("A soma dos números é: ",soma) 

    
