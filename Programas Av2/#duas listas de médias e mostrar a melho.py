#duas listas de médias e mostrar a melhor 

p1 = []
p2 = []
n = int(input("Qual o tamanho da turma? "))
print("*"*20)

for i in range (n):
    n1 = float(input("Digite a nota da P1: "))

    p1.append(n1)

print("*"*20)

for i in range (n):
    n2 = float(input("Digite a nota da P2: "))

    p2.append(n2)

m1 = (sum(p1))/n
m2 = (sum(p2))/n

if m1>m2:
    maior = "turma 1"

else:
    maior = "turma 2"

print ("P1 = ", p1)
print ("P2 = ", p2)            
print ("Média da turma na prova 1: ", m1)
print ("Média da turma na prova 2: ", m2)
print("A turma ",maior," obeteve a melhor média.")