#Aula 09 de tuplas - Curso Udemy
year = ("janeiro","fevereiro","março","abril","maio", "junho", "julho", "agosto", "setembro" ,"outubro","novembro","dezembo")
birth = input("Digite a sua data de nascimento:")
index = int(birth[3:5])-1
month = year[index]
print(month)  

#Aula 10 de dicionários
#Dicionário de cores primárias
paleta = {"vermelho":"red", "amarelo":"yellow", "verde":"green"}
cor = input("Insira o nome de uma cor em português:").lower()
print(paleta.get(cor,"Essa cor não consta na paleta."))

#Aula 017 - Loops
#Faça um código para registrar uma venda. O programa vai receber do usuário o nome do produto e o preço, e vai adicioná-lo á fatura. Em seguida, pergunte ao usuário se ele quer compra mais algum produto.
#Se a resposta for sim, repitaa operação. Só pare quando a resposta for "Não", e então imprima a fatura, que deve conter os produtos comprados e os preços. Ao final, deve apresentar o total da fatura.

repetir = "s"
fatura = []
total = 0

while repetir == "s":
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    fatura.append([produto, preco])
    total += preco
    repetir = input("Deseja comprar mais algum produto? (s ou n)").lower()

    for i in fatura:
        print(i[0],"-",i[1])

print("O total da fatura é:R$", total)

#Validação de dados
#Aula 18 - Necessário para verificação dos tipos de dados digitados na inserção de preços

repetir = "s"
fatura = []
total = 0
valid_preco = False

while repetir == "s":
    produto = input("Digite o nome do produto: ") 
    while valid_preco == False:
        preco = input("Digite o preço do produto: ")
        try:
            preco = float(preco)
            if preco<=0:
                print("O preço precisa ser maior que zero.")
            else:
                    valid_preco = True
        except:
            print("Formato de preço inválido. Use apenas números e separe os centavos com '.'.")
    fatura.append([produto, preco])
    total += preco
    valid_preco = False
    repetir = input("Deseja comprar mais algum produto? (s/n)").lower()
for i in fatura:
    print(i[0], "- R$", i[1])
print("O preço total é: R$", total)

#Validação de dados
#Aula 19

nome = input("Digite o nome do aluno: ")

valid_nota = False
while valid_nota == False:
    nota1 = float(input("digite a nota da prova 1: "))
    try:
        nota1 = float(nota1)
        if nota1 < 0 or nota1 >10:
            print("Nota inválida. O valor deve estar entre 0 e 10.")
        else:
            valid_nota = True 
    except:
        print("Nota inválida. Use apenas números e separe os decimais com ponto.")

valid_nota = False
while valid_nota == False:
    nota2 = float(input("Digite a nota da prova 2: "))
    try:
        nota2 = float(nota2)
        if nota2 < 0 or nota2 >10:
            print("Nota inválida. O valor deve estar entre 0 e 10.")
        else:
            valid_nota = True
    except:
        print("Nota inválida. Use apenas números e separe os decimais com ponto.")

valid_faltas = False
while valid_faltas == False:
    faltas = int(input("Digite o total de faltas: "))
    try:
        faltas = float(faltas)
        if faltas <0 or faltas >20:
            print("Número de faltas inválido. Valor deve ser entre 0 e 20.")
        else:
            valid_faltas = True
    except:
        print("Número de faltas inválido. Use apenas números.")

        
media = (nota1+nota2)/2
assid = (20-faltas)/20

if media >= 6 and assid >= 0.7:
    resultado = "Aprovado."
elif media < 6 and assid <0.7:
    resultado = "Reprovado por média e falta."
elif media < 6:
    resultado = "Reprovado por média."
elif assid < 0.7:
    resultado = "Reprovado por falta."
else:
    print("erro.")

print("Nome: ",nome)
print("Média: ", media)
print("Assiduidade: ", str(assid*100)+"%")
print("Resultado: ", resultado)