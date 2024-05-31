'''
A classe cliente tem:

- endereço;
- e tem uma lista de contas - que é do tipo conta;
- 2 operações:
  - o primeiro é realizar transação - ele recebe dois atributos, que seria uma conta e a transação, onde a conta é do tipo conta e a transação é do tipo aqui da classe que estava na transação, então pode ser um saque, passar um depósito, mas a gente vai olhar ai para saber se temos um **polimorfismo**.
  - Adicionar conta - lembrando que o meu cliente pode ter várias contas, e com várias contas onde a conta é relacionada a um cliente e temos uma **generalização**.
'''

class cliente:
  def __init__(self, endereco):
    self.endereco = endereco
  
    # cpf = input("Informe o CPF (somente número): ")
    # cliente = filtrar_cliente(cpf, clientes)

    # if cliente:
    #     print("\n@@@ Já existe cliente com esse CPF! @@@")
    #     return

    # nome = input("Informe o nome completo: ")
    # data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    # endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    # cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    # clientes.append(cliente)

    # print("\n=== Cliente criado com sucesso! ===")