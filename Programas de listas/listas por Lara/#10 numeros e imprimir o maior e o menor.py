#10 numeros e imprimir o maior e o menor 


lista = []

for i in range (10):
    numero = int(input("Digite um número: "))
    lista.append(numero)

print("O menor número é: ", min(lista))
print("O maior número é: ", max(lista))