# Criando a lista notas 
notas  = []

for contador in range(0,4):
    valor = int(input("Insira uma nota: "))
    notas.append(valor)

print ("lista notas: ", notas)

#soma os elementos e calcula media
media = (sum(notas) / 4)
print ("Média das notas digitadas ", media)

