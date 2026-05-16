# Autor: Ana Luiza
# Projeto: Condicionais

#Definição das variáveis
nome= input('Digite seu nome:')
primeira_nota= float(input('Digite sua nota:'))
segunda_nota= float(input('digite sua nota:'))
media=(primeira_nota+segunda_nota)/2
if media >= 6:
    print(f'{nome} sua nota é {media} - Aluno Aprovado!')
else:
    print('Aluno Reprovado!')
