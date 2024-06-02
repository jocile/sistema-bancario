from abc import ABC, abstractmethod

from MyApp.models import Conta


class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta: Conta):
        pass
