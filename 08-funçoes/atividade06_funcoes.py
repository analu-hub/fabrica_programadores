# Declaração de variáveis
valor1 = float(input('digite o primeiro valor: '))
valor2 = float (input('digite o segundo valor: '))

# função  calcular - 4 operações básicas
def calcular (valor1,valor2):
    somar = valor1+valor2
    subtrair = valor1-valor2
    multiplicar = valor1*valor2
    dividir = valor1/valor2
    print(f'o resultado é: {somar}')
    print(f'o resultado é: {subtrair}')
    print(f'o resultado é: {multiplicar}')
    print(f'o resultado é: {dividir}')

# chamada da função
calcular(valor1,valor2)