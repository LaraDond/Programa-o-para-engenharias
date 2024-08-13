#4 notas de 10 alunos, mostrar media de cada um e contar maiores de 7

lista = []
notas_mais_que_7 = 0

for i in range(10):
    nome = input("Digite o nome do aluno: ")
    soma = 0

    for notas in range(4):
        nota = float(input("Digite a nota do aluno: "))
        lista.append(nota)
        soma += nota

    media = soma/4    
    if media >= 7 :
        notas_mais_que_7 += 1

    print(nome, " tem média = ", media)
    print("*"*25)

print(notas_mais_que_7, " alunos tem média maior ou igual a 7.")        


