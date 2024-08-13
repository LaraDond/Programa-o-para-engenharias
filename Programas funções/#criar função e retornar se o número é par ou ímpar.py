#criar função e retornar se o número é par ou ímpar

def verificar (n):
    if n%2 == 0:
        print("Número par")

    else:
        print("Número ímpar")

while True:
    num = int(input("Digite um número: "))
    verificar(num)
    continuar = input("Deseja continuar? (S ou N): ").upper()
    print("*****************")
   
    if continuar == "N":
        break
          
