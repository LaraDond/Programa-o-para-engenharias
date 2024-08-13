# Criando as listas
A = []
B = []
C = []

#contador para lista C 
indice = 0

for contador in range(5):
    valor1 = int(input("Digite um valor lista A: "))
    A.append(valor1)
    valor2 = int(input("Digite um valor lista B: "))
    B.append(valor2)
    #intercalar os valores de A e B na lista C
    C.insert(indice, valor1)
    indice +=1
    C.insert(indice, valor2)
    indice +=1
    
print ("lista A     : ", A)
print ("lista B     : ", B)
print ("lista C (intercalar A e B) : ", C)


