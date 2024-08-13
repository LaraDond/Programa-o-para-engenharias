def calcular_media(n1,n2,n3):
    media = (n1 + n2 + n3) / 3
    return media

def verificar_situacao(resul):
    if resul > 6:
        print ("Situação do aluno: Aprovado!")
    if resul >= 4  and  r <= 6:
        print ("Situação do aluno: Em Recuperação!")
    if resul < 4:
        print ("Situação do aluno: Reprovado!")
    return 

while  True:
       nome  = input("Digite nome do aluno:  ")
       nota1 = float(input('entre com a primeira  nota:  '))
       nota2 = float(input('entre com a segunda   nota:  '))
       nota3 = float(input('entre com a terceira  nota:  '))
       
       #chamada da funcao calcular media
       resultado = calcular_media(nota1,nota2,nota3)
       print ("Aluno: ",nome," Média final : ",resultado)
       
       #chamada da funcao situação aluno
       verificar_situacao(resultado)
   
       opcao = input("Deseja continuar S ou N ? ").upper()
       if opcao == "N":
            break
