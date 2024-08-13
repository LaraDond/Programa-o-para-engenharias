# Criando a lista idades 
idades = []

for contador in range(0,5):
    valor = int(input("Insira a idade aluno: "))
    idades.append(valor)

print ("Lista de idades : ",idades)

#inverte a lista do menor pro maior numero
idades.sort(reverse=False)
print ("Lista de idades Decrescente : ",idades)

#inverte a lista do maior pro menor numero
idades.sort(reverse=True)
print ("Lista de idades crescente : ",idades)
