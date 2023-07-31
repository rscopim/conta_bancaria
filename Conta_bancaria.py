saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

print("Selecione o número da opção desejada: ")

while True:

    opcao = int(input("Digite sua opção (1 - Depositar, 2 - Sacar, 3 - Extrato, 4 - Sair): \n"))

    if opcao == 1 :
        valor = float(input("Informe o valor do deposito: "))
        if valor > 0:
            saldo = valor
            extrato = "" f"Depósito: R$ {valor: .2f}\n"
        else:
            print("Operação fahou! O valor informado é inválido.")

    elif opcao == 2:
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação fahou! O valor informado é inválido.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == 4:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


    