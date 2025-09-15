nome_usuario = input("Digite seu nome: ")
idade_usuario = int(input("Digite sua idade: "))
possui_carteira = input("Possui carteira de motorista?: \n (1-Sim / 2-Não)")

if idade_usuario >= 18:
    if possui_carteira == "1":
        print("Autorizado")
    else:
        print("Não autorizado")
else:
    print("Individuo é menor de idade")