#criar função e retornar se o número é positivo ou negativo

def verificar (n):
    if n>0:
        print("Número positivo")

    else:
        print("Número negativo")

while True:
    num = int(input("Digite um número: "))
    verificar(num)
    continuar = input("Deseja continuar? (S ou N): ").upper()
    print("*****************")
   
    if continuar == "N":
        break
          
    
