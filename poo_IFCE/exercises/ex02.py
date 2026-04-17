class Conta:
    """
    Classe que permite a criação de um objeto CONTA BANCÁRIA.
    """
    def __init__(self, numero, nome, saldo = 0, limite = 0):
        self.id = numero
        self.titular = nome
        self.saldo = saldo
        self.limite = limite
        print(f"Conta {numero} criada com sucesso.")

    def depositar(self, value):
        self.saldo += value
        print(f"Depósito de valor R$ {value:.2f} autorizado.")

    def sacar(self, value):
        if self.saldo >= value:
            self.saldo -= value
            print(f"Saque de valor R$ {value:.2f} autorizado.")
        else:
            print(f"SAQUE NEGADO | Saldo indisponível")

    def atualiza_limite(self, novo_limite):
        self.limite += novo_limite
        print(f'Limite atualizado ! Atual = R$ {self.limite}')

    def extrato(self):
        print(f"A conta {self.id} de {self.titular} possui R$ {self.saldo:.2f} e limite R$ {self.limite}.")

# Objetos
contaUm = Conta(1010, "Hiury", 1700, 1000)
contaUm.extrato()

print('\n')

contaUm.atualiza_limite(500)
contaUm.extrato()

