#Criando as variáveis
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso: "))

#Calculando o IMC 

imc= peso / (altura**2)

#Exibe o resultado

print ("O seu IMC é: (: .if)",format (imc))

#Clasifica o IMC

if imc <= 18.5:
    print("Classificação: Abaixo do peso")

elif imc <= 24.9:
    print("Classificação: peso normal")

elif imc <= 29.9:
    print("Classificação: sobrepeso")

elif imc <= 34.9:
    print("Classificação: obesidade grau 1")

elif imc <= 39.9:
    print("Classificação: obesidade grau 2")

else: 40 <= imc < 40
print("Classificação: obsidade grau 3(Mórbida)")




    




    



