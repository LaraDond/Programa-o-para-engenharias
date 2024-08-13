#ler uma lista e verificar se um número esta nela

def verificar(lis,para):
    if para in lis:
        return True
    else:
        return False

    
lista = []

while True:
    valor = int(input("Digite um valor: "))
    lista.append(valor)

    continuar = input("Deseja continuar? (S ou N): ").upper()
    print("***********************")

    if continuar == "N":
        break
    
parametro = int(input("Digite o valor parametro: "))

resultado = verificar(lista,parametro)

print("O número está presente na lista? ",resultado) 
