# Criando as listas
alunos = []

for contador1 in range(5):
    nota1 = float(input("Digite nota1 do aluno: "))
    alunos.append(nota1)
    nota2 = float(input("Digite nota2 do aluno: "))
    alunos.append(nota2)
    media = (nota1 + nota2 ) / 2
    print ("média do aluno = ",media)

print ("lista de notas : ", alunos)


