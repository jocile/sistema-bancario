import textwrap

from MyApp.controllers import util


class __main__:
    clientes = []
    contas = []

    @staticmethod
    def menu():
        menu = """\n
        ================ MENU ================
        [d]\tDepositar
        [s]\tSacar
        [e]\tExtrato
        [nc]\tNova conta
        [lc]\tListar contas
        [nu]\tNovo usuário
        [q]\tSair
        => """
        return input(textwrap.dedent(menu))

    @staticmethod
    def main():
        while True:
            opcao = __main__.menu()
            if opcao == "d":
                util.depositar(__main__.clientes)

            elif opcao == "s":
                util.sacar(__main__.clientes)
            elif opcao == "e":
                util.exibir_extrato(__main__.clientes)
            elif opcao == "nu":
                util.criar_cliente(__main__.clientes)
            elif opcao == "nc":
                numero_conta = len(__main__.contas) + 1
                util.criar_conta(numero_conta, __main__.clientes, __main__.contas)
            elif opcao == "lc":
                util.listar_contas(__main__.contas)
            elif opcao == "q":
                break
            else:
                print(
                    "\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@"
                )


if __name__ == "__main__":
    main = __main__()
    main.main()
