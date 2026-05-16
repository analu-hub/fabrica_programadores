# Autor: Ana Luiza
# Projeto: Condicionais

#Definição das variáveis
nome= input('Digite seu nome:')
peso= float(input('Digite seu peso:'))
altura= float (input('Digite sua altura'))

imc=peso/(altura*altura)
if imc <= 18.5:
    print('esta abaixo do peso!')
else:
    print('esta peso normal!')
