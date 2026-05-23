peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))

imc = peso / (altura ** 2)

print(f"IMC: {imc:.2f}")

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 24.9:
    print("Classificação: Peso normal")
elif imc < 29.9:
    print("Classificação: Sobrepeso")
elif imc < 34.9:
    print("Classificação: Obesidade Grau I")
elif imc < 39.9:
    print("Classificação: Obesidade Grau II")
else:
    print("Classificação: Obesidade Grau III (mórbida)")