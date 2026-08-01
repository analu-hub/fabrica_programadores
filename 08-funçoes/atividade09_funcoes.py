# Projeto:Cafeteria Aroma e Sabor usando função

# Definição das variaveis
nome = input("Digite o nome do cliente")
pedido = int(input("escolha sua bebida: 1-café ou 2-chá"))

def preparar_bebida():
    if pedido == 1:
        print(nome, ", seu café está pronto!")
    else:
        print(nome, ", seu chá está pronto!")

preparar_bebida()