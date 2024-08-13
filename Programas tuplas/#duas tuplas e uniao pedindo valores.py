#duas tuplas e uniao pedindo valores

n = int(input("Digite numero deseja inserir: "))

tuplaA = ()
tuplaB = ()
tuplaC = ()

for contador in range(n):
    valor = int(input("Digite número tupla A:"))
    tuplaA = tuplaA + tuple([valor])

for contador in range(n):
    valor = int(input("Digite número tupla B:"))
    tuplaB = tuplaB + tuple([valor])

tuplaC = tuplaA + tuplaB

print("Tupla A:", tuplaA)
print("Tupla B:", tuplaB)
print("Tupla C:", tuplaC)

    
    
                
