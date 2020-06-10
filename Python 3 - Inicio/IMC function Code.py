#Definindo funções
#Aula 21

def imc(peso, altura):
    imc = (peso/(altura*altura))
    return imc

def class_imc(sexo, peso, altura):
    valor_imc = imc(peso, altura)

    if sexo == "m":
        if valor_imc < 20.7:
            return "Abaixo do peso."
        elif valor_imc >=20.7 and valor_imc < 26.4:
            return "Peso normal."
        elif valor_imc >=26.4 and valor_imc < 27.8:
            return "Maginalmente acima do peso."
        elif valor_imc >=27.8 and valor_imc < 31.1:
            return "Obesidade."
        else:
            return "Erro de cálculo. Entre em contato com o administrador."

    if sexo == "f":
        if valor_imc < 19.1:
            return "Abaixo do peso."
        elif valor_imc >=19.1 and valor_imc < 25.8:
            return "Peso normal."
        elif valor_imc >=25.8 and valor_imc < 27.3:
            return "Marginalmente acima do peso."
        elif valor_imc >=27.3 and valor_imc < 32.2:
            return "Acima do peso ideal."
        elif valor_imc >=32.2:
            return "Obesidade."
        else:
            "Erro de cálculo.Entre em contato com o administrador."

#Código começa a funcionar a partir daqui, pois acima só foram definições de funções
print("Vamos calcular o seu imc?")
valid_sexo = False
while valid_sexo == False:
    sexo = input("Digite o seu sexo (M ou F):").lower()
    if sexo != "m" and sexo !="f":
        print("Inválido. Digite M ou F.")
    else:
        valid_sexo = True

valid_peso = False
while valid_peso == False:
    peso = input("Digite o peso (ex. 68.5): ")
    try:
        peso = float(peso)
        if peso <= 0 or peso > 350:
            print("Peso inválido. Número não pode ser zero ou negativo, e deve ser inferior a 350kg.")
        else:
            valid_peso = True
    except:
        print("Peso inválido. Use apenas números, e separe casas decimais com ponto.")

valid_altura = False
while valid_altura == False:
    altura = input("Digite a altura (ex. 2.5): ")
    try:
        altura = float(altura)
        if altura <=0 or altura >3:
            print("Altura inválida. Número não pode ser zero ou negativo, e deve ser inferior a 3 metros.")
        else:
            valid_altura = True
    except:
        print("Altura inválida. Use apenas números e separe os decimais com ponto.")

resultado1_imc = imc(peso, altura)
resultado2_imc = class_imc(sexo, peso, altura)

print("O seu IMC é: {:.2f}.".format(resultado1_imc))
print("A sua classificação é: {}.".format(resultado2_imc))