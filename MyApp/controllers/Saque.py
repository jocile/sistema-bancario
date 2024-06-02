from MyApp.controllers.Transacao import Transacao
from MyApp.models.Conta import Conta


class Saque(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta: Conta):
        """Lógica para realizar o saque na conta
         e registrar no histórico

        Realiza um saque na conta especificada.

        Args:
            valor (float): O valor a ser sacado.
            conta (Conta): A conta da qual o saque será realizado.

        Returns:
            bool: True se o saque foi realizado com sucesso, False caso contrário.
        """
        if self._valor > conta.saldo:
            print("Saldo insuficiente para realizar o saque.")
            return False

        conta.saldo -= self._valor
        print(f"Saque de R${self._valor:.2f} realizado com sucesso.")
        return True
