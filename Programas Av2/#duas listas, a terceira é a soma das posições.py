#duas listas, a terceira é a soma das posições

lista1= []
lista2=[]

for i in range (6):
    n1 = int(input("Digite número para lista 1: "))
    lista1.append(n1)

print("*****************************")

for i in range (6):
    n2 = int(input("Digite número para lista 2: "))
    lista2.append(n2)

s0= lista1[0]+lista2[0]
s1= lista1[1]+lista2[1]
s2= lista1[2]+lista2[2]
s3= lista1[3]+lista2[3]
s4= lista1[4]+lista2[4]
s5= lista1[5]+lista2[5]  

lista3 = [s0,s1,s2,s3,s4,s5]

print("*****************************")
print("Lista 1: ", lista1)
print("Lista 2: ", lista2)
print("Lista 3: ", lista3)

