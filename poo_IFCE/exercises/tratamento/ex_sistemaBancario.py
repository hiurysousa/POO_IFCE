'''
# 24) Sistema bancário:
# Crie a classe conta com o método sacar chamando a função validar_saldo.
# Capture exceção, caso ocorra e registre log simples.
# Repropague exceção para camada superior do programa.
'''

class SaldoInsuficienteError(Exception):
    pass

class Conta:
    def __init__(self, saldo):
        self._saldo = saldo

    def validar_saldo(self, valor):
        if valor > self._saldo:
            raise SaldoInsuficienteError(f'Saldo insuficiente. Valor em conta: R${self._saldo}')

    def sacar(self, valor):
        try:
            self.validar_saldo(valor)
            self._saldo -= valor
            print(f'Saque de R$ {valor} realizado com sucesso.')
        except SaldoInsuficienteError as e:
            print(f'Tentativa de saque NEGADA. {e}')

            raise

try:
    minha_conta = Conta(200)
    minha_conta.sacar(250)
except SaldoInsuficienteError:
    print(f'A camada superior recebeu o erro e pode exibir um alerta.')

