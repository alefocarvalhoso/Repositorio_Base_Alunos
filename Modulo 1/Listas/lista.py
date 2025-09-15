cadastro = []
def cadastrar(cadastro):
    nome = input("Digite o nome: ")
    cadastro.append(nome)
    print(f"usuario {nome} cadastrado !")

def listar(cadastro):
    print('--------------------')  
    for i, nome in enumerate(cadastro, start=1):  
        print(f"{i}. {nome} ")
    print('--------------------')  

def remover(cadastro):
        nome = input("Digite o nome: ")
        cadastro.remove(nome)
        print(f"usuario {nome} excluido !")

while True:
    print("1 - Cadastrar usuario")
    print("2 - listar usuario")
    print("3 - remover usuario")
    print("0 - sair")
    opcao = input("Digite a opção")

    if opcao == "1":
        cadastrar(cadastro)

    elif opcao == "2":
        listar(cadastro)

    elif opcao == "3":
        remover(cadastro)
        
    elif opcao == "0":
         break
                             