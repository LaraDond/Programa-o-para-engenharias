#ler um numero e apresetar algorismos q o num tem 

numero =input("Digite um número entre 100 e 999: ")

dic = {}

for i in numero:
    if i in dic:
        dic[i] +=1

    else:
        dic[i] = 1

print("Os algorismos e quantidades são: ", dic) 
