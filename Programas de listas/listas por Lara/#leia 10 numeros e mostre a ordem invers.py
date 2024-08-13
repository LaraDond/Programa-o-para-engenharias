#leia 10 numeros e mostre a ordem inversa

lista = []

for i in range (10):
    numeros = int(input("Digite um número inteiro:"))
    lista.append(numeros)

print("Ordem normal:", lista)
lista.reverse()
print("Ondem inversa: ", lista)