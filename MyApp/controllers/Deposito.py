from MyApp.controllers import Transacao


class Deposito(Transacao):
    def __init__(self, valor: float)->float:
        self._valor = valor

    def valor(self):
        return self._valor

    def registrar(self, conta):
        # Lógica para realizar o saque na conta
        # e registrar no histórico
        pass