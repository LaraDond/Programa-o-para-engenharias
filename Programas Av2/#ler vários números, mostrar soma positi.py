#ler vários números, mostrar soma positivos, média, maior e menor número

lista_positivos = []
contador = 0 

while True:
    numero = int(input("Digite um número: "))

    if numero<0:
        break

    contador += 1
    lista_positivos.append(numero)

soma = sum(lista_positivos)
print("Lista de números: ",lista_positivos)
print("Soma dos números: ", soma)
print("Média: ", soma/contador)
print("Menor número: ", min(lista_positivos))
print("Maior número: ", max(lista_positivos))
