# loop while com função
def tabuada(numero):
    i = 1
    while i <= 10:
        print(f'{numero} x {i} = {numero * i}')
        i += 1

numero = int(input('Digite um número para ver a tabuada: '))
tabuada(numero)