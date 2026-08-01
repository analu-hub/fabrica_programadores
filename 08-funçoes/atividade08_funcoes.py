# Definição das variáveis

nome = input('Digite seu nome:')
nota = float(input('Digite sua nota:'))  

def verificar_aprovacao(nota):
    if nota >= 6:
        print('Aluno Aprovado!')
    else:
        print('Aluno Reprovado!')

#chamada da funçao
verificar_aprovacao(nota)