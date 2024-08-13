#digitar frase e contar letras:

frase = input("Digite uma frase para contar as letras: ")

contagem_caracteres = {}

for caractere in frase:
    # Se o caractere já estiver no dicionário, incrementa o contador
    if caractere in contagem_caracteres:
        contagem_caracteres[caractere] += 1
    # Se não estiver, adiciona o caractere ao dicionário com contagem 1
    else:
        contagem_caracteres[caractere] = 1

print("Resposta:", contagem_caracteres)

    