#10 letras e contar vogais e consoantes 

lista = []
vogal = 0 
consoante = 0

for i in range(10):
    letras = input("Digite uma letra: ")
    lista.append(letras)

    if letras.upper() == "A" or letras.upper() =="E"or letras.upper() =="I"or letras.upper() =="O"or letras.upper() =="U":
        vogal += 1

    else:
        consoante += 1 

print("Vogal = ", vogal)
print("Consoante = ", consoante)            
