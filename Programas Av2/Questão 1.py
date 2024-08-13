#Questão 1

lista = []
lista_par = []

n = int(input("Digite quantos números você deseja inserir: "))

for i in range (n):
    numero = int(input("Digite um número positivo: "))

    lista.append(numero)

    if numero%2 ==0:
        lista_par.append(numero)

print("A lista é: ",lista)
print("A soma dos pares da lista é: ", sum(lista_par))

    

