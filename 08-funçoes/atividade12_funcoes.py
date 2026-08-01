# Desafio adicional
def analisar_emprestimo(valor, taxa, meses):
    montante = valor * (1 + taxa) ** meses
    juros = montante - valor
    limite_juros = valor * 0.10
