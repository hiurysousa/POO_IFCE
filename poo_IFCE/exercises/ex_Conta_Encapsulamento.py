'''
# 12) Crie a classe ContaBancaria com o atributo privado chamado __saldo.
# Use o decorador @property para criar um getter para saldo.
# Crie um @saldo.setter que impeça depósitos de valores negativos.
# Lance um ValueError caso o valor informado seja menor que zero.
# Teste a proteção tentando atribuir um valor inválido ao saldo.
'''

class ContaBancaria:

    def __init__(self, titular:int, saldo:float, limite:float):
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def setter_saldo(self, valor:float):
        if valor < 0:
            raise ValueError("Saldo não pode ser negativo.")
        self.__saldo = valor

    @property
    def titular(self):
        return self.__titular


minha_conta = ContaBancaria(1010, 500, 1500)

print(f'Saldo da conta {minha_conta.titular}: {minha_conta.saldo}')


