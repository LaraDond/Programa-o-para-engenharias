#50 pessoas, nome , altura, sexo e peso ideal

i = 1
M = 0
F = 0

while (i <= 50):
    nome = input("Digite seu nome: ")
    altura = float(input("Digite sua altura: "))
    sexo = input("Digite seu sexo, use F para feminino e M para masculino: ")

    if (sexo.upper() ==  "M"):
        peso = ((72.7 * altura)-58)
        print("Seu peso ideal é: ", peso)
        M += 1

    if (sexo.upper() == "F"):
        peso = ((62.1 * altura)-44.7)
        print("Seu peso ideal é: ", peso)
        F += 1
        
    print("*************************")    

    i += 1

print("Total masculino = ", M)
print("Total feminino = ", F)

    
    

    
                   
