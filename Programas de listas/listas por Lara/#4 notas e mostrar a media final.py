#4 notas e mostrar a media final

lista = []

for i in range (4):
    nota = float(input("Digite o valor da nota: "))
    lista.append(nota)

soma = sum(lista)

print("A média do aluno é: ", soma/4)