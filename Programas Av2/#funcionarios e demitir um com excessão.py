#funcionarios e demitir um com excessão

dic = {}

for i in range(2):
    cod = int(input("Digite o código: "))
    nome = input("Digite o nome: ").upper()
    funcao = input("Digite a função: ").upper()
    tempo_anos = int(input("Digite o tempo de serviço, em anos: "))

    lista = []
    lista.append(nome)
    lista.append(funcao)
    lista.append(tempo_anos)

    dic.update({cod:lista})

print("Funcionários: ",dic)
demitir = int(input("Digite o cadastro do funcionário que você deseja demitir: "))

if demitir in dic:
    funcionario = dic[demitir]
    if funcionario[1] == "PROGRAMADOR" and funcionario[2] >= 3:
        print("Este funcionário não pode ser demitido!")
    else:
        dic.pop(demitir)
        print(f"Funcionário {funcionario[0]} foi demitido com sucesso!")

        # Mostrar os funcionários restantes
        print("Funcionários restantes:", dic)