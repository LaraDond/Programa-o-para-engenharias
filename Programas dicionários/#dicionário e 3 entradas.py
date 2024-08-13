#dicionário e 3 entradas

d = {}

while True:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo, 'f' para feminino e 'm' para masculino: ")
    continuar = input("Deseja continuar, 's' para sim e 'n' para não: ")
#criar lista
    contato = []
    contato.append(idade)
    contato.append(sexo)
    d.update ({nome:contato})

    if continuar.upper() == "N":
        break
print("O dicionário que você criou é: ",d)

    
              
    
