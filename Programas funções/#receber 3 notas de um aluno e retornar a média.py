#receber 3 notas de um aluno e retornar a média

def calcular_media(nota1, nota2, nota3):
    media_total = (nota1+nota2+nota3)/3
    return media_total

nome = input("Digite o nome do aluno: ")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = calcular_media(n1,n2,n3)

print("A média final é: ", media)
