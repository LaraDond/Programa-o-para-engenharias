#Questão 3

dic = {}
alunos_mais_50_freq = 0

while True:
    codigo = int(input("Digite seu código (0 para sair): "))

    if codigo == 0:
        break
    
    nome = input("Digite seu nome: ")
    nota = float(input("Digite sua nota: "))
    freq = int(input("Digite sua frequência (número de aulas que esteve presente): "))
    print("***************************")

    if freq > 50:
        alunos_mais_50_freq += 1
        
    lista = []
    lista.append(nome)
    lista.append(codigo)
    lista.append(freq)

    dic.update({nota:lista})

print("***********************")
print("Aluno com maior nota: ", dic[max(dic, key=dic.get)])
print("Aluno com menor nota: ", dic[min(dic, key=dic.get)])
print("Quantidade alunos com mais de 50 dias de frequência: ", alunos_mais_50_freq)

      
    
                 
