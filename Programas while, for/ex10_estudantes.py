#contadores
totalEI  = 0
totalEF1 = 0
totalEF2 = 0
totalEM  = 0
print ("Pesquisa sobre Nível Escolar ")
print ()
while True:
    print ("********************************")
    print ("Escolha seu Nível Escolar: ")
    print ("EI  = Educação Infantil    ")
    print ("EF1 = Ensino Fundamental 1 ")
    print ("EF2 = Ensino Fundamental 2 ")
    print ("EM  = Ensino Médio         ")
    print ("S - Sair Programa          ")
    opcao = input("Escolha a opção desejada; ").upper()
    if (opcao == "S"):
        print ("Fim do programa.....")
        break   
    nome = input("Digite nome estudante; ")
    print ("********************************")
    if (opcao == "EI"):
        totalEI += 1
    if (opcao == "EF1"):
        totalEF1 += 1
    if (opcao == "EF2"):
        totalEF2 += 1
    if (opcao == "EM"):
        totalEM += 1
print ("********************************")
print ("Total estudantes Ensino Infantil     = ",totalEI)
print ("Total estudantes Ensino Fundamental1 = ",totalEF1)
print ("Total estudantes Ensino Fundamental2 = ",totalEF2)
print ("Total estudantes Ensino Médio        = ",totalEM)
