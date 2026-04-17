# classe (Conta bancária com numero, nome, saldo (permite depositar e sacar))
import rich
class Account:
    """
    Classe que permite a criação de um objeto CONTA BANCÁRIA.
    """
    def __init__(self, numero, nome, saldo = 0):
        self.id = numero
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {numero} criada com sucesso.")

    def depositar(self, revenue):
        self.saldo += revenue
        print(f"Depósito de valor R$ {revenue:.2f} autorizado.")

    def sacar(self, revenue):
        if self.saldo >= revenue:
            self.saldo -= revenue
            print(f"Saque de valor R$ {revenue:.2f} autorizado.")
        else:
            print(f"SAQUE NEGADO | Saldo indisponível")

    def __str__(self):
        return f"A conta {self.id} de {self.titular} possui R$ {self.saldo:.2f}"

# Objetos
contaUm = Account(1010, "Hiury", 1700)
print("\n")
contaUm.depositar(200)
print("\n")
contaUm.sacar(2500)
print("\n")
print(contaUm)

rich.inspect(contaUm)