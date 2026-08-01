penta = ['Brasil','Paraguay','chile']
tetra = ['Brasil','Italia','Alemanha']
tri = ['Brasil','Italia','Alemanha','Argentina']

# imprimindo os nomes
print ('--- Campeões do Mundo---')

# excluindo por posição
# exemplo: excluir o chile
print(penta)
del penta[2]
print(penta)

# excluindo por nome
print(penta)
penta.remove('Paraguay')
print(penta)