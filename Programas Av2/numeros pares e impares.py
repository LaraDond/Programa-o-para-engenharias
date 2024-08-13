#numeros pares e impares:

par = []
impar = []
contador_impar = 0
soma_par = 0

for i in range (6):
    num = int(input("Digite um número: "))

    if num%2 == 0:
        par.append(num)
        soma_par += num

    else:
        impar.append(num)
        contador_impar +=1

print("Pares: ", par)
print("Ímpares: ", impar)
print("Soma pares: ", soma_par)
print("Quantidade ímpares: ", contador_impar)    

