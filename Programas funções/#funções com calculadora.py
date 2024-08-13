#funções com calculadora

def adicao(a,b):
    adi = a+b
    return adi

def subtracao(a,b):
    sub = a-b
    return sub

def multiplicacao(a,b):
    mult = a*b
    return mult

def divisao(a,b):
    div = a/b
    return div

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

print("• adição (opção 1)")
print("• subtração (opção 2) ")
print("• multiplicação (opção 3)")
print("• divisão (opção 4)")

opcao = int(input("Digite o número da opção: "))

if opcao == 1:
    resultado  = adicao(n1,n2)
    print("O resultado da adição é: ", resultado)

if opcao == 2:
    resultado  = subtracao(n1,n2)
    print("O resultado da subtração é: ", resultado)
    
if opcao == 3:
    resultado  = multiplicacao(n1,n2)
    print("O resultado da multiplicação é: ", resultado)

if opcao == 4:
    resultado  = divisao(n1,n2)
    print("O resultado da divisão é: ", resultado)    
    


    
