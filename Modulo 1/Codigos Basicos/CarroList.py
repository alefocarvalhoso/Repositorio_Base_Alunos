variaveis_aceitas = ['honda', 'chverolet']




escolha = input("[1] Mostrar lista de carros")



def cadastrar_carro():
    novo_carro = input("Digite o nome do carro: ")
    variaveis_aceitas.append(novo_carro)
    print(variaveis_aceitas)
