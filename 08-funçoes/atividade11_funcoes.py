# loop for com função
def tabuada(numero, inicio, fim):
    for i in range(inicio, fim + 1):
        print(f'{numero} x {i} = {numero * i}')

numero = int(input('Digite a tabuada desejada: '))
inicio = int(input('Digite o primeiro número da tabuada: '))
fim = int(input('Digite o último número da tabuada: '))

tabuada(numero, inicio, fim)