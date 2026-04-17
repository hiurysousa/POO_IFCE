'''
Crie a classe ContaCorrente com os atributos privados __titular, __saldo e __limite.
Use @property para criar getters para os três atributos.
O __saldo não pode ser negativo e o __limite deve estar entre 0 e 10000, lançando ValueError em ambos os casos.
Crie o método sacar(valor) que impeça saques acima do saldo disponível e o método depositar(valor) que
impeça depósitos negativos ou zerados. Armazene em uma lista __historico todas as
operações realizadas com uma descrição e exiba o histórico ao final.
'''

class ContaCorrente:
    def __init__(self, titular:str, saldo:float, limite:float):
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__historico = []

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @saldo.setter
    def saldo(self, valor:float):
        if valor < 0:
            raise ValueError('Não é possível tornar um saldo negativo.')
        self.__saldo = valor

    @limite.setter
    def limite(self, valor:float):
        if valor < 0 or valor > 10000:
            raise ValueError('Valor do limite deve estar entre 0 e 10000.')
        self.__limite = valor

    def depositar(self, valor:float):
        if valor <= 0:
            raise ValueError('Não é possível depositar valor 0 ou negativo.')
        self.__saldo += valor
        historico_dict = {'acao':'deposito', 'valor':valor}
        self.__historico.append(historico_dict)

    def sacar(self, valor:float):
        if valor > self.__saldo:
            raise ValueError('Não é possível sacar acima do valor da conta.')
        self.__saldo -= valor
        historico_dict = {'acao': 'saque', 'valor': valor}
        self.__historico.append(historico_dict)

    def historico(self):
        i = 1
        for log in self.__historico:
            print(f'Registro {i}: {log}')
            i += 1

conta_hiury = ContaCorrente('Hiury', 1000, 1500)
print(f'Titular: {conta_hiury.titular} || Saldo: {conta_hiury.saldo} || Limite: {conta_hiury.limite}')
conta_hiury.depositar(200)
conta_hiury.depositar(100)
conta_hiury.sacar(50)
print(f'Titular: {conta_hiury.titular} || Saldo: {conta_hiury.saldo} || Limite: {conta_hiury.limite}')

conta_hiury.historico()

