import os


while True:
    # Limpa a tela
    os.system('cls')  # no Windows
    # os.system('clear')  # no Linux/macOS

    # Menu
    print("=== MENU ===")
    print("1 - Dizer Olá")
    print("2 - Mostrar soma")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        print("Olá! 😊")
    elif opcao == "2":
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        print(f"A soma é {a + b}")
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")

    input("Pressione Enter para voltar ao menu...")