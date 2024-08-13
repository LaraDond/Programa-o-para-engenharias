#4 notas de 10 alunos, armazenar média em lista

lista = []
contador = 0

for i in range(10):
    nome = input("Digite o nome do aluno: ")
    media = []

    for i in range(1):
        n1 = float(input("Digite a primeira nota: "))
        n2 = float(input("Digite a segunda nota: "))
        n3 = float(input("Digite a terceira nota: "))
        n4 = float(input("Digite a quarta nota: "))
        print("****************************")

        valor_media = (n1+n2+n3+n4)/4
        media.append(valor_media)

        if valor_media >= 7:
            contador += 1 

    lista.append(media)  

print("A lista de médias é: ", lista)
print("Quantidade alunos média >= 7:",contador)
