import textwrap

from MyApp.controllers import Deposito, Saque
from MyApp.models.Conta_corrente import ContaCorrente
from MyApp.models.Pessoa_fisica import PessoaFisica


class util:

    @staticmethod
    def filtrar_cliente(cpf, clientes):
        clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
        return clientes_filtrados[0] if clientes_filtrados else None

    @staticmethod
    def recuperar_conta_cliente(cliente):
        if not cliente.contas:
            print("\n@@@ Cliente não possui conta! @@@")
            return

        # FIXME: não permite cliente escolher a conta
        return cliente.contas[0]

    @staticmethod
    def depositar(clientes):
        cpf = input("Informe o CPF do cliente: ")
        cliente = util.filtrar_cliente(cpf, clientes)

        if not cliente:
            print("\n@@@ Cliente não encontrado! @@@")
            return

        valor = float(input("Informe o valor do depósito: "))
        transacao = Deposito(valor)

        conta = util.recuperar_conta_cliente(cliente)
        if not conta:
            return

        cliente.realizar_transacao(conta, transacao)

    @staticmethod
    def sacar(clientes):
        cpf = input("Informe o CPF do cliente: ")
        cliente = util.filtrar_cliente(cpf, clientes)

        if not cliente:
            print("\n@@@ Cliente não encontrado! @@@")
            return

        valor = float(input("Informe o valor do saque: "))
        transacao = Saque(valor)

        conta = util.recuperar_conta_cliente(cliente)
        if not conta:
            return

        cliente.realizar_transacao(conta, transacao)

    @staticmethod
    def exibir_extrato(clientes):
        cpf = input("Informe o CPF do cliente: ")
        cliente = util.filtrar_cliente(cpf, clientes)

        if not cliente:
            print("\n@@@ Cliente não encontrado! @@@")
            return

        conta = util.recuperar_conta_cliente(cliente)
        if not conta:
            return

        print("\n================ EXTRATO ================")
        transacoes = conta.historico.transacoes

        extrato = ""
        if not transacoes:
            extrato = "Não foram realizadas movimentações."
        else:
            for transacao in transacoes:
                extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

        print(extrato)
        print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
        print("==========================================")

    @staticmethod
    def criar_cliente(clientes):
        cpf = input("Informe o CPF (somente número): ")
        cliente = util.filtrar_cliente(cpf, clientes)

        if cliente:
            print("\n@@@ Já existe cliente com esse CPF! @@@")
            return

        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input(
            "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): "
        )

        cliente = PessoaFisica(
            nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco
        )

        clientes.append(cliente)

        print("\n=== Cliente criado com sucesso! ===")

    @staticmethod
    def criar_conta(numero_conta, clientes, contas):
        cpf = input("Informe o CPF do cliente: ")
        cliente = util.filtrar_cliente(cpf, clientes)

        if not cliente:
            print(
                "\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@"
            )
            return

        conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
        contas.append(conta)
        cliente.contas.append(conta)

        print("\n=== Conta criada com sucesso! ===")

    @staticmethod
    def listar_contas(contas):
        for conta in contas:
            print("=" * 100)
            print(textwrap.dedent(str(conta)))
