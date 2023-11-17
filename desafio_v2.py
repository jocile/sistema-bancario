import textwrap

def menu():
    menu = """
    [d]: Depositar,
    [s]: Sacar,
    [e]: Extrato,
    [u]: Criar usuário,
    [c]: Criar conta,
    [m]: Mostrar contas,
    [x]: Sair
    Digite a opção => """
    return input(menu)

def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Realizado o depósito de R$ {valor:.2f}")
    else:
        print("Valor de depósito inválido!")
    return saldo

def sacar(*, saldo, extrato, limite, LIMITE_SAQUES, numero_saques):
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
        print(f"Realizado o saque de R$ {valor:.2f}") 
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, numero_saques

def mostrar(saldo, /, *, extrato):
    print("======== EXTRATO ========")
    if len(extrato) == 0:
        print('Não foram realizadas movimentações.')
    else:
        for indice, movimentacao in enumerate(extrato):
            print(f"{indice+1}: {movimentacao}")
        print(f'\nSaldo atual: R$ {saldo:.2f}')                
    print("===============================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    for usuario in usuarios :
        if usuario["cpf"] == cpf :
            print("usuário já cadastrado com esse CPF!")
            return
        
    nome = input("Digite o nome: ")
    endereco = input("Endereço: ")
    data_nascimento = input("Data de nascimento: ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário cadastrado com sucesso!")

def criar_conta(agencia, contas, usuarios):
    cpf = input("Digite o CPF do usuário: ")
    for usuario in usuarios :
        if usuario["cpf"] == cpf :
            numero_conta = len(contas) + 1
            contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
            print(f"A conta de {usuario["nome"]} foi criada!")
            return
    print("Usuário não cadastrado com esse CPF!")

def mostrar_contas(agencia, contas):
    print(f"Agência: {agencia}")
    for conta in contas:        
        linha = f"""            
            Conta: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print("--------------------")
        print(textwrap.dedent(linha))

def main(): 
    agencia = 1
    saldo = 0
    limite = 500
    extrato = []
    usuarios = []
    contas = []

    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = menu() 
        if opcao == "d":
            saldo = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, numero_saques = sacar(saldo=saldo, extrato=extrato, limite=limite, LIMITE_SAQUES=LIMITE_SAQUES, numero_saques=numero_saques)
        elif opcao == "e":
            mostrar(saldo, extrato = extrato)
        elif opcao == "u":
            criar_usuario(usuarios)
        elif opcao == "c":
            criar_conta(agencia, contas, usuarios)
        elif opcao == "m":
            mostrar_contas(agencia, contas)
        elif opcao == "x":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()