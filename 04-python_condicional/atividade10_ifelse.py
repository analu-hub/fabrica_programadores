nome = input("Digite seu nome: ")
telefone = input("Digite seu telefone: ")
cidade = input("Digite sua cidade: ")
salario = float(input("Digite seu salário: "))

if salario > 1000:
    print(nome + ", você possui uma renda boa")
elif salario > 700 and salario <= 1000:
    print(nome + ", você possui uma renda razoável")
elif salario > 500 and salario <= 700:
    print(nome + ", você possui uma renda baixa")
else:
    print(nome + ", você possui uma renda muito baixa")