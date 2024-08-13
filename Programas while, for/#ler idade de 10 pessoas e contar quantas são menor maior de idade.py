#ler idade de 10 pessoas e contar quantas são menor/maior de idade

maiorid = 0
menorid = 0

for contador in range (0,10):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    print("**************************")

    if (idade < 18):
        menorid += 1

    else:
        maiorid += 1

print(maiorid, " pessoas são maiores de idade e ",menorid," pessoas são menores de idade.")
        
        
                
