# Criando a lista notas 
medias = []

n = int(input("Quantos alunos deseja cadastrar médias: "))

for contador in range(0,n):
    valor = input("Insira uma nota: ") 
    medias.append(valor)

print ("Nr de alunos: ",n)
print ("Lista de médias digitados : ",medias)
