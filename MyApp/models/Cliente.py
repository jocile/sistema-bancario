

from MyApp.controllers import Transacao
from MyApp.models import Conta


class cliente:
  def __init__(self, endereco:str, contas:list):
    self.endereco = endereco
    self.contas = contas
    
  def realizar_transacao(self, conta: Conta, transacao: Transacao):
    """
        Realiza uma transação em uma conta do cliente.

        Args:
            conta (Conta): Conta na qual a transação será realizada.
            transacao (Transacao): Objeto de transação a ser realizada.
        """
    transacao.registrar(conta)
  
  def adicionar_conta(self, conta: Conta):
    """
        Adiciona uma nova conta ao cliente.

        Args:
            conta (Conta): Conta a ser adicionada.
        """
    self.contas.append(conta)