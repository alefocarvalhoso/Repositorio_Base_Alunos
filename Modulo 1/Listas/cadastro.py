import time

# ---------- LOGIN ----------
def login():
    print("-----------------------------------")
    print("****** 🔐 SISTEMA DE ACESSO 🔐 ******")
    print("-----------------------------------")
    
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    print("Verificando credenciais...")
    time.sleep(1)

    if usuario == "admin" and senha == "1234":
        print("✅ Login bem-sucedido!")
        print(f"Bem-vindo, {usuario}!")
        return True
    else:
        print("❌ Usuário ou senha incorretos.")
        return False

# ---------- SISTEMA DE CADASTRO ----------
def cadastrar_nome(cadastro):
    novo_nome = input("Digite o nome da pessoa: ")
    cadastro.append(novo_nome)
    print(f"✅ Usuário {novo_nome} foi adicionado!")

def menu():
    cadastro = []
    while True:
        print("\n---------- SISTEMA DE CADASTRO -----------")
        print("[1] Cadastrar nome")
        print("[2] Listar nomes")
        print("[3] Excluir nome")
        print("[0] Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_nome(cadastro)
        elif opcao == '2':
            print("\n📋 Lista de nomes cadastrados:")
            if not cadastro:
                print("Nenhum nome cadastrado ainda.")
            for i, nome in enumerate(cadastro, start=1):
                print(f"{i}. {nome}")
        elif opcao == '3':
            excluir_nome = input("Digite o nome para excluir: ")
            if excluir_nome in cadastro:
                cadastro.remove(excluir_nome)
                print(f"🗑️ {excluir_nome} foi removido.")
            else:
                print("⚠️ Nome não encontrado.")
        elif opcao == '0':
            print("👋 Saindo do sistema...")
            break
        else:
            print("❗ Opção inválida. Tente novamente.")

# Executando
if login():
    menu()