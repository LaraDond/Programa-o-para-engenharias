#pesquisa nivel escolar
print("NÍVEL ESCOLAR:")
print("EI  = Educação Infantil")
print("EF1 = Ensino Fundamental 1")
print("EF2 = Ensino Fundamental 2")
print("EM  = Ensino Médio")
print("Digite '3' em 'nome' para encerrar pesquisa.")
print("**********************")

nome = 0
ei = 0
ef = 0
ef2 = 0
em = 0

while (nome != "3"):
    nome = input("Digite seu nome: ")
    ne = input("Digite seu nível escolar: ")
    
    print("**************************")
   
    if (ne.upper() == "EI"):
        ei+=1

    if (ne.upper() == "EF1"):
        ef += 1

    if (ne.upper() == "EF2"):
        ef2 += 1

    if (ne.upper() == "EM"):
        em += 1    

   
print("FIM DE PROGRAMA")
print("Resultado da pesquisa:")
print("EI = ",ei)
print("EF1 = ",ef)
print("EF2 = ",ef2)
print("EM = ",em)

    

       


    

