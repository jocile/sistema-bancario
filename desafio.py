menu = {
    "[d]": "Depositar",
    "[s]": "Sacar",
    "[e]": "Extrato",
    "[q]": "Sair"
}

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    print("\nMENU:")
    for opcao, descricao in menu.items():
        print(f"{opcao}] {descricao}")
    opcao = input("Digite a opção: ")

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")

        else:
            print("Valor de depósito inválido!")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato.append(f"Saque: R$ {valor:.2f}")
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if len(extrato) == 0:
            print('Não foram realizadas movimentações.')
        else:
            print('\nExtrato:')
            for indice, movimentacao in enumerate(extrato):
                print(f"{indice+1}: {movimentacao}")
            print(f'\nSaldo atual: R$ {saldo:.2f}\n')                
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")