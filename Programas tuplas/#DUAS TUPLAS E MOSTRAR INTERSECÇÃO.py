#DUAS TUPLAS E MOSTRAR INTERSECÇÃO

n = int(input("Digite quantos valores você deseja inserir na primeira: "))
s = int(input("Digite quantos valores você deseja inserir na segunda: "))

tupla1 = ()
tupla2 = ()
tupla3 = ()

for i in range (n):
    valor = int(input("Digite o valor A: "))
    tupla1 = tupla1 + tuple([valor])

for i in range (s):
    valor = int(input("Digite o valor B: "))
    tupla2 = tupla2 + tuple([valor])

    if valor in tupla1:
        tupla3 = tupla3 + tuple([valor])
    

print("A intersecção é: ", tupla3)
