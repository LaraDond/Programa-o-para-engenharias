# Criando as listas
alunos = []
soma = 0

for contador1 in range(10):
    soma = 0
    for contador2 in range(2):
        nota = float(input(f"Digite nota do aluno: "))
        alunos.append(nota)
        soma += nota
    media = soma / 2
    print ("média do aluno = ",media)

print ("lista de notas : ", alunos)


