from MyApp.controllers.Transacao import Transacao
from MyApp.models.Conta import Conta


class Deposito(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta: Conta):
        """Lógica para realizar o saque na conta
         e registrar no histórico
        Registra um deposito na conta especificada.

        Args:
            conta (Conta): A conta para depositar o valor.

        Returns:
            bool: True se o depósito foi bem sucedido, False se mal sucedido.
        """

        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
            return True
        return False
