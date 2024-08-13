#lista com 10 valores e remover os ímpares

lista = []
lista2 = []

for i in range (10):
    valor = int(input("Digite um número: "))
    lista.append(valor)

    if valor%2 == 0:
        lista2.append(valor)

print("Lista normal: ",lista)
print("Nova lista: ", lista2)