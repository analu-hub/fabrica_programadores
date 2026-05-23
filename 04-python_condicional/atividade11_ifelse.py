nome = input("Digite o nome da pessoa: ")
idade = int(input("Digite a idade: "))
cnh = input("Possui CNH? (sim/não): ").lower()

if idade < 18:
    print(f"{nome} é menor de idade.")
elif cnh == "sim":
    print(f"{nome} pode dirigir.")
else:
    print(f"{nome} não pode dirigir.")