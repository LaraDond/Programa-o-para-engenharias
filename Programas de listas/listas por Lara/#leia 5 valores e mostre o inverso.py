#leia 5 valores e mostre o inverso 

lista = []

for i in range (5):
    valor = float(input("Digite um valor: "))
    lista.append(valor)

print("A lista original é: ", lista)
print("A lista invertida é: ", lista.reverse())



