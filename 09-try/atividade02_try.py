try:
    valor1=float(input('converter BRL em dolar:'))
    dolar=valor1 / 5.08
    print(f'BRL convertido: {dolar}')
except:
    print('coloque apenas numeros.')