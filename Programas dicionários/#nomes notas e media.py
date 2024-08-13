#nomes notas e media

dic = {}
n = int(input("Quantos alunos deseja cadastrar: "))

for i in range(n):
    print("*************************")
    nome = input("Digite o nome do aluno: ")
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    
    lista = []
    lista.append(n1)
    lista.append(n2)
    lista.append(n3)

    dic.update({nome:lista})
    
    media = (sum(lista))/3
    if media >=7:
        print("Aluno: ",nome," está aprovado.")
    if media <7:
        print("Aluno: ",nome," em recuperação.")
    if media<5:
        print("Aluno: ",nome," está reprovado.")

print("Lista de alunos e notas: ",dic)        
        
        


    
               
        
