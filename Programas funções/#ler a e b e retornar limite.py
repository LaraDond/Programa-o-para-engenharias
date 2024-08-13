#ler a e b e retornar limite

def imprimir_dados(A,B,lim):
    if (A + B) > lim:
        return True

    else:
        return False

while True:
    valorA = int(input("Digite o primeiro valor: "))
    valorB = int(input("Digite o segundo valor: "))
    limite = int(input("Digite o valor limite: "))

    resultado = imprimir_dados(valorA,valorB,limite)

    print("Soma primeiro valor mais segundo valor é maior que o limite? ", resultado)

    opcao = input("Deseja continuar?(S ou N): ").upper()

    if opcao == "N":
        break
    


