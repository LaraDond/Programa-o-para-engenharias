print("DB - Diabetes")
print("HP - Hipertensão")
print("CO - Colesterol Alto")
print("AS – Asma")
print("NP – Não possui doença")
print("Digite '5' no campo 'nome' para sair.")
print("*"*12)


quantidade = 0
m = 0
f = 0
db = 0
hp = 0
co = 0
AS = 0
np = 0

while True:
    nome = input("Digite seu nome: ")

    quantidade += 1    

    if nome == "5":
        print("Fim de programa!")
        break

    sexo = input("Digite seu sexo, 'M' para masculino e 'F' para feminino: ")
    doenca = input("Digite sua doença (DB, HP, CO, AS OU NP): ")
    print("*"*12)

 

    if sexo.upper() == "M":
        m += 1

    if sexo.upper() == "F":
        f += 1

    if doenca.upper() == "DB":
        db += 1

    if doenca.upper() == "HP":
        hp += 1 

    if doenca.upper() == "CO":
        co += 1  

    if doenca.upper() == "AS":
        AS += 1   

    if doenca.upper() == "NP":
        np += 1  

    
print("Total de entrevistados: ",quantidade - 1)
print("Tipos de doenças e quantidade de pessoas:")
print("Diabetes: ", db)
print("Hipertensão: ", hp) 
print("Colesterol Alto: ", co)
print("Asma: ", AS)
print("Não possui doença: ", np)
print("Sexos registrados:")
print("Masculino: ", m)
print("Feminino: ",f)
    







