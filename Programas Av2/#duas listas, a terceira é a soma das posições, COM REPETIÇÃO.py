#duas listas, a terceira é a soma das posições

lista1= []
lista2=[]
lista3 = []

for i in range (6):
    n1 = int(input("Digite número para lista 1: "))
    lista1.append(n1)

print("*****************************")

for i in range (6):
    n2 = int(input("Digite número para lista 2: "))
    lista2.append(n2)

for i in range(0,6):
    soma = lista1 [i] + lista2 [i]
    lista3.append(soma)

print("*****************************")
print("Lista 1: ", lista1)
print("Lista 2: ", lista2)
print("Lista 3: ", lista3)