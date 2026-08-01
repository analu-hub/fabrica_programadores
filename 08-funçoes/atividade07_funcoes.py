# Definição das variáveis
altura = float(input('digite sua altura:'))
peso = float(input('Digite seu peso:'))

# calcular o IMC usando a fórmula:peso/(altura ao quadrado)
def calcular(peso,altura):
    imc = peso/(altura**2)
    print(f'seu IMC é: {imc}')

calcular(peso,altura)