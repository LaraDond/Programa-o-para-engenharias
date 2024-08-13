#temperaturas do ano e mostrar acima da media 

dic = {}
lista = []

for i in range (4):
    mes = input("Digite o mês do ano: ")
    temperatura = float(input("Digite a temperatura média do mês:"))

    dic.update({mes:temperatura})
    lista.append(temperatura)

media = (sum(lista))/4  

print(dic)
print("A média do ano é: ", media)
print("Os meses que ultrapassaram a temperatura média são: ")

for mes, temperatura in dic.items():
    if temperatura>media:
        print(mes,"-",temperatura)
    

