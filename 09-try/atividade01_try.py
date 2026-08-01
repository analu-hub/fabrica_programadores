# Autor: Ana
# Projeto: Entendendo tratamento de exceção
try:
  valor1 = float(input('Digite o primeiro valor'))
  valor2 = float(input('Digite o segundo valor'))
  soma = valor1+valor2
  print(f'o resultado da soma é:{soma}')
except:
    print('Digite apenas números.')