# Entrada de dados
nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3

# Verificação da situação
if media >= 7:
    situacao = "Aprovado"
elif media > 4:
    situacao = "Em Recuperação"
else:
    situacao = "Reprovado"

# Saída
print("\nAluno:", nome)
print("Média:", round(media, 2))
print("Situação:", situacao)