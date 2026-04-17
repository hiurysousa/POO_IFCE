'''
Você foi contratado para desenvolver um sistema de pagamentos.
Todo pagamento possui um titular e um valor.
Existem dois tipos de pagamento: cartão de crédito e boleto.
A classe base deve se chamar Pagamento e as classes derivadas CartaoCredito e Boleto.
Crie a classe base com os atributos titular e valor, e um método exibir_resumo() que exiba essas informações
sem precisar ser sobrescrito. Crie o método processar_pagamento() como abstrato,
onde cada subclasse deve exibir uma mensagem específica de como aquele pagamento é processado.
Instancie um objeto de cada subclasse e chame os dois métodos.
'''

from abc import ABC, abstractmethod
class Pagamento(ABC):
    def __init__(self, titular:str, valor:float):
        self.__titular = titular
        self.__valor = valor

    def exibir_resumo(self):
        print(f'Titular: {self.__titular} || Valor: {self.__valor}')

    @abstractmethod
    def processar_pagamento(self):
        pass

class CartaoCredito(Pagamento):
    def processar_pagamento(self):
        print(f'Pagamento realizado com cartão de crédito necessita de limite disponível e permite parcelamento.')

class Boleto(Pagamento):
    def processar_pagamento(self):
        print(f'Pagamento via boleto é pago somente à vista e leva de 2 a 3 dias para ser confirmado no sistema.')

pagamento_um = CartaoCredito('1010', 1500)
pagamento_um.exibir_resumo()
pagamento_um.processar_pagamento()

pagamento_dois = Boleto('2020', 150)
pagamento_dois.exibir_resumo()
pagamento_dois.processar_pagamento()
