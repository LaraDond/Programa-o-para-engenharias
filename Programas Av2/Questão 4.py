#Questão 4

lista = []

while True:
    temperatura = float(input("Digite uma temperatura: "))
    continuar = input("Deseja continuar? (S/N):").upper()
    print("********************")

    lista.append(temperatura)
    
    if continuar == "N":
        break

media = (sum(lista))/ (len(lista))

print("********************")
print("A menor temperatura foi de: ",min(lista))
print("A maior temperatura foi de: ", max(lista))
print("A média de temperaturas foi de: ",media)
    
