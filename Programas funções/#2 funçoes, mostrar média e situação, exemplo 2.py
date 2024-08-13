#2 funçoes, mostrar média e situação, exemplo 2

def calcular_media(nota1, nota2, nota3):
    media_total = (nota1+nota2+nota3)/3
    return media_total

def aprovação(med):
    if media > 6:
        print("Aprovado.")

    elif media <= 6:
        print("Verificação Suplementar.")
        
    else:
        print("Reprovado.")
    

nome = input("Digite o nome do aluno: ")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = calcular_media(n1,n2,n3)
status = aprovação(media)

print("A média final é: ", media)
