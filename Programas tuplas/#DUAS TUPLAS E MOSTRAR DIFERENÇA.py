#DUAS TUPLAS E MOSTRAR DIFERENÇA

n = int(input("Digite quantos valores você deseja inserir na primeira: "))
s = int(input("Digite quantos valores você deseja inserir na segunda: "))

tupla1 = ()
tupla2 = ()
tupla3 = ()

for i in range (n):
    valorA = int(input("Digite o valor A: "))
    tupla1 = tupla1 + tuple([valorA])

for i in range (s):
    valor = int(input("Digite o valor B: "))
    tupla2 = tupla2 + tuple([valor])

    if valor not in tupla1:
        tupla3 = tupla3 + tuple([valor])
        
for i in tupla1:
    if i not in tupla2:
        tupla3 = tupla3 + tuple([i])
        
    
print("A diferença entre tuplas é: ", tupla3)
