#tupla de vendas

Vendas = (120, 130, 100, 110, 90, 120, 111, 80, 140, 120, 90, 120)

n = 12
soma = 0

for i in tupla:
    soma += i

media = soma/n
variancia = ((soma - media)**2)/n
desvio = variancia**(1/2)

print("Lista: ", vendas)
print("Média: ", media)
print("Variância: ", variancia)
print("Desvio: ", desvio)