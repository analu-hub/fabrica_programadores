# Programa Agenda em Python
agenda = []
resposta = "s"
while resposta == "s":
    nome = input("Digite um novo nome: ")
    agenda.append(nome)
    resposta = input("Deseja cadastrar outro nome? (s/n): ")
print("Nomes cadastrados:")
print(agenda)
