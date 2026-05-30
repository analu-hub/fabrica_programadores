numero= int(input('Digite a tabuada desejada:'))
inicio = int(input('Digite o primeiro numero da tabuada '))
fim = int(input('Digite o ultimo numero da tabuada'))

for i in range(inicio,fim+1):
    print(f'{numero} x {i} = {numero * i}')