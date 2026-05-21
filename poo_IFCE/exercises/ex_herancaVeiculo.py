'''
Você foi contratado por uma empresa para desenvolver um sistema de gerenciamento de veículos.
Cada veículo possui características como marca, modelo e ano. Existem dois tipos de veículos no sistema: carros
e motocicletas. A classe base deve ser chamada de Veiculo, e as classes derivadas devem ser chamadas de Carro
e Motocicleta. Crie a classe base Veiculo com os atributos marca, modelo e ano. Crie o método exibir_dados()
na classe base. Crie as subclasses Carro e Motocicleta que herdam de Veiculo. Cada uma deve implementar o
método emitir_som(), exibindo uma mensagem específica para o tipo de veículo, como "Buzina de carro" ou
"Som de motocicleta".
O programa deve instanciar um objeto de cada subclasse e exibir as informações e sons correspondentes.
'''

from abc import ABC, abstractmethod

class AnoNegativo(Exception):
    def __init__(self, ano):
        super().__init__(f'{ano} é um valor inválido. Try again.')

class Veiculo(ABC):
    def __init__(self, marca, modelo, ano):
        if ano < 0:
            raise AnoNegativo(ano)
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @abstractmethod
    def emitir_som(self):
        pass

    @abstractmethod
    def exibir_dados(self):
        pass

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)

    def emitir_som(self):
        print(f'Buzina de carro...')

    def exibir_dados(self):
        print(f'CARRO -> {self.marca} | {self.modelo} | {self.ano}')

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)

    def emitir_som(self):
       print(f'Buzina de moto...')

    def exibir_dados(self):
        print(f'MOTO -> {self.marca} | {self.modelo} | {self.ano}')

try:
    carro_um = Carro('Honda', 'Civic', -2009)
    carro_um.emitir_som()
    carro_um.exibir_dados()
    print(f'\n')
    moto_um = Moto('Honda', 'Biz', 2015)
    moto_um.emitir_som()
    moto_um.exibir_dados()
except Exception as e:
    print(f'{e}')