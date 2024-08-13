#10 numeros e remover numeros já digitados 

lista = []

for i in range (10):
    num = int(input("Digite um número: "))

    if num not in lista:
        lista.append(num)   

print("A lista final é: ", lista)