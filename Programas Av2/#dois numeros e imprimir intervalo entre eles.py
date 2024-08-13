#duas entradas e imprimir valores entre eles 

lista = []

x = int(input("Digite um número: "))
y = int(input("Digite outro número, sendo este maior que o primeiro: "))

for i in range(x,y+1):
    lista.append(i)

print("O intervalo entre os números é: ", lista)
