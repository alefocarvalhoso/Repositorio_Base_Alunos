cadastro = []
while True:
    print("1 - Cadastrar usuario")
    print("2 - listar usuario")
    print("3 - remover usuario")

    opcao = input("Digite a opção")
    if opcao == "1":
        nome = input("Digite o nome: ")
        cadastro.append(nome)
        print(cadastro)

