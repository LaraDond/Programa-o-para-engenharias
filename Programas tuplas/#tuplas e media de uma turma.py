#tuplas e media de uma turma

turma1 = int(input("Digite o número de alunos da turma 1: "))
turma2 = int(input("Digite o número de alunos da turma 2: "))

tupla1 = ()
tupla2 =()
soma1 = 0
soma2 = 0

for i in range (turma1):
    nota1 = float(input("Digite a nota turma 1: "))
    tupla1 = tupla1 + tuple([nota1])
    soma1 += nota1

for i in range (turma2):
    nota2 = float(input("Digite a nota turma 2: "))
    tupla2 = tupla2 + tuple([nota2])
    soma2 += nota2

print("Média turma 1 = ",soma1/turma1)

print("Média turma 2 = ",soma2/turma2)    
