# Autor: Ana Luiza
# Projeto: Condicionais

#Definição das variáveis
nome = input('Digite seu nome:')
idade = float(input('Digite sua idade:'))
produto = float(input('Digite o preço do produto'))
if produto >= 100:
    preco=produto *0.10
else:
    preco=produto *0.5
print("Nome:", nome)
print("Idade:", idade)
print("Valor calculado:", preco)