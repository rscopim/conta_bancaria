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
            print("Operação negada! O valor informado é inválido.")

    elif opcao == 2:
        valor = float(input("Informe o valor do saque: "))
        saldo_excedido = valor > saldo
        limite_excedido = valor > limite
        saques_excedidos = numero_saques > LIMITE_SAQUES

        if saldo_excedido:
            print("Operação negada! Você não possui saldo para essa transação.")
        elif limite_excedido:
            print("Operação negada! O valor do saque excede o limite disponivel.")
        elif saques_excedidos:
            print("Operação negada! Número máximo de saques diários excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação negada! O valor informado é inválido.")

    elif opcao == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == 4:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


    