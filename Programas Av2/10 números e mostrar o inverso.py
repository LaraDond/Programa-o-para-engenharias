#lista de 10 números e mostrar na ordem inversa

lista = []

for i in range(0,10):
    valor = int(input("Digite um número: "))

    lista.append(valor)

print("Ordem normal: ", lista)
lista.reverse()
print("Ordem inversa: ", lista)
