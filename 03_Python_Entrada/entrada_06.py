#  Autor: Ana luiza
# Projeto: IMC com input e f-string

# Declaração de variáveis
peso = float(input('digite o seu peso: '))
altura = float (input('digite a sua altura: '))
imc = peso / (altura * altura)

# exibindo os resultados
print(f'seu IMC é: {imc:.2f}')