try:
    valor1=float(input('converter Celsius e fahrenheit:'))
    conversao=(valor1 * (9/5)+32)
    print(f'Celsius convertido: {conversao}')
except:
    print('coloque apenas numeros.')