#exercicio tabuada com for

numero = int(input("Digite um número: "))

for contador in range(1,11):
    resultado = numero * contador
    print(numero, "x",contador,"=", resultado)

#com for não precisa usar i += 1   

print("Fim do programa")
    
