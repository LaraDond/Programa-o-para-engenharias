#4 funcionários e tirar um

dic = {}

for i in range (4):
    codigo = int(input("Digite o código do funcionário: "))
    nome = input("Digite o nome do funcionário: ")
    print("******************************************")

    dic[codigo] = nome
    
print("Os funcionários são: ",dic)
demitir = int(input("Digite o código do funcionário que deseja demitir: ")) 
dic.pop(demitir)

print("Os funcionários restantes são: ",dic)

    
     
