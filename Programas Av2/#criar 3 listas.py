#criar 3 listas

lista1 = []
lista2 = []
lista3 = []
for i in range(0,5):
    valor = int(input("Digite valor lista 1: "))

    lista1.append(valor)
    lista3.append(valor)


for i in range(0,5):
    valor2 = int(input("Digite valor lista 2: "))

    lista2.append(valor2)
    lista3.append(valor2)

lista3.sort (reverse = False)
print("Lista 1: ", lista1)
print("Lista 2: ", lista2)
print("Lista 3: ", lista3)