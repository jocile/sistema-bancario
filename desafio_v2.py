def menu():
    menu = """\n
    "[d]": "Depositar",
    "[s]": "Sacar",
    "[e]": "Extrato",
    "[x]": "Sair"
    Digite a opção => """
    return input(menu)

def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        return saldo
    else:
        print("Valor de depósito inválido!")

def sacar(saldo, extrato, limite, LIMITE_SAQUES, numero_saques):
    valor = float(input("Informe o valor do saque: "))
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1        
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, numero_saques

def mostrar(extrato, saldo):
    print("======== EXTRATO ========")
    if len(extrato) == 0:
        print('Não foram realizadas movimentações.')
    else:
        for indice, movimentacao in enumerate(extrato):
            print(f"{indice+1}: {movimentacao}")
        print(f'\nSaldo atual: R$ {saldo:.2f}')                
    print("===============================")

def main():    
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = menu() 
        if opcao == "d":
            saldo = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, numero_saques = sacar(saldo, extrato, limite, LIMITE_SAQUES, numero_saques)
        elif opcao == "e":
            mostrar(extrato, saldo)
        elif opcao == "x":
            break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

main()