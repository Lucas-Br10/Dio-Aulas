# Sistema Bancário Básico
saldo = 0
limite_saque = 500
extrato = []
opcao = ""

def exibir_menu():
    print("\n--- MENU BANCO ---")
    print("1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")

while opcao != "4":
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor_deposito = float(input("Digite o valor do depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato.append(f"Depósito: R${valor_deposito:.2f}")
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido. Tente novamente.")

    elif opcao == "2":
        valor_saque = float(input("Digite o valor do saque: "))
        if valor_saque <= saldo and valor_saque <= limite_saque:
            saldo -= valor_saque
            extrato.append(f"Saque: R${valor_saque:.2f}")
            print("Saque realizado com sucesso!")
        elif valor_saque > saldo:
            print("Saldo insuficiente!")
        elif valor_saque > limite_saque:
            print(f"O limite por saque é de R${limite_saque:.2f}")

    elif opcao == "3":
        print("\n--- EXTRATO ---")
        if extrato:
            for item in extrato:
                print(item)
        else:
            print("Nenhuma movimentação registrada.")
        print(f"Saldo atual: R${saldo:.2f}")

    elif opcao == "4":
        print("Encerrando o sistema bancário. Obrigado por utilizar!")
    else:
        print("Opção inválida. Por favor, escolha novamente.")