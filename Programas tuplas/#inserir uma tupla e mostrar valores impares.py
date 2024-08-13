#inserir uma tupla e mostrar valores impares

tupla = ()

for i in range (10):
    valor = int(input("Digite um valor inteiro: "))

    if (valor%2) != 0:
        tupla = tupla + tuple([valor])

print(tupla)

        
    
