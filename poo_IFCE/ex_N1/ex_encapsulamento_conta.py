class ContaBancaria:

    def __init__(self, titular:str, saldo:float, limite:float):
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def exibir_saldo(self) -> None:
        print(f'Saldo Atual: {self.__saldo}')

    def depositar(self, valor:float) -> None:
        self.__saldo += valor

    def sacar(self, valor:float) -> bool:
        if valor <= self.__saldo:
            self.__saldo -= valor
            return True
        return False

    @property
    def get_titular(self) -> str:
        return self.__titular


minha_conta = ContaBancaria('1010', 1500, 1000)
print(f'Titular da conta {minha_conta.get_titular}')
minha_conta.exibir_saldo()
minha_conta.depositar(200)
minha_conta.exibir_saldo()
