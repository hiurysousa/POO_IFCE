'''
ContaBancaria
--------------
- numero:int
- titular: str
- saldo: float
- limite: float
--------------
+ ContaBancaria(numero:int, titular:str, saldo_inicial: float = 0.0, limite = 1000.0)
+ obter_saldo()
+ obter_limite()
+ novo_limite(valor:float)
+ depositar(valor:float)
+ sacar(valor:float)
+ extrato()
'''

class ContaBancaria:
    def __init__(self, numero:int, titular:str, saldo_inicial = 0, limite = 1000):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo_inicial
        self.__limite = limite

    def obter_saldo(self):
        return self.__saldo

    def obter_limite(self):
        return self.__limite

    def novo_limite(self, valor:float):
        self.__limite = valor

    def depositar(self, valor:float):
        self.__saldo += valor

    def sacar(self, valor:float):
        self.__saldo -= valor

    def extrato(self):
        print(f'Saldo atual: {self.__saldo}')


conta = ContaBancaria(1234, 'Maria Oliveira', 500, 2000)
conta.depositar(300)
conta.sacar(900)
conta.extrato()