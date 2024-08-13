# Criando a lista caracteres 
caracteres  = []

#criar contadores de vogais e consoantes
totalVogais = 0
totalConsoantes = 0

for contador in range(0,10):
    letra = input("Insira uma letra: ").upper()
    caracteres.append(letra)
    if letra == "A" or letra == "E" or letra == "I" or  letra == "O" or letra == "U" :
           totalVogais += 1
    else :
           totalConsoantes += 1

print ("lista digitadas     : ", caracteres )
print ("Total de Vogais     : ", totalVogais)
print ("Total de Consoantes : ", totalConsoantes)

