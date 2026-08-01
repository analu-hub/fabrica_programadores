# Autor: Ana
# projeto: trabalhando
# funcionario.txt
# nome| email | telefone | salario
# salario - carga_horaria * valor_hora
# carga_horaria = 200
# valor_hora = 22.22

carga_horaria = 200
valor_hora = 22.22
salario = carga_horaria * valor_hora

nome = input("Nome: ")
email = input("Email: ")
telefone = input("Telefone: ")

arquivo = open("funcionario.txt", "a")
arquivo.write(nome + "|" + email + "|" + telefone + "|" + str(salario) + "\n")
arquivo.close()

print("Cadastro realizado!")
print("Nome:", nome)
print("Salário: R$", salario)