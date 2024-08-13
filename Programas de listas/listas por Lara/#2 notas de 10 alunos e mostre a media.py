#2 notas de 10 alunos e mostre a media

lista = []

for i in range(10):
    nome = input("Digite o nome do aluno: ")
    soma = 0 

    for i in range(2):
        nota = float(input("Digite uma nota: "))
        lista.append(nota)
        soma += nota

    print("Nome = ", nome)
    print("Média = ", soma/2)    
    print('*'*20)