# Definição das variáveis


# calcular o IMC usando a fórmula:peso/(altura ao quadrado)
try:
    altura = float(input('digite sua altura:'))
    peso = float(input('Digite seu peso:'))
    def calcular(peso,altura):
        imc = peso/(altura**2)
        print(f'seu IMC é: {imc}')

    calcular(peso,altura)
except:
    print('erro')