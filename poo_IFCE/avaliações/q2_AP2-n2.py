'''
Você foi contratado por uma empresa para desenvolver um sistema de gerenciamento de veículos.
Cada veículo possui características como marca, modelo e ano. Existem dois tipos de veículos no sistema: carros
e motocicletas. A classe base deve ser chamada de Veiculo, e as classes derivadas devem ser chamadas de Carro
e Motocicleta. Crie a classe base Veiculo com os atributos marca, modelo e ano. Crie o método exibir_dados()
na classe base. Crie as subclasses Carro e Motocicleta que herdam de Veiculo. Cada uma deve implementar o
método emitir_som(), exibindo uma mensagem específica para o tipo de veículo, como "Buzina de carro" ou
"Som de motocicleta".
O programa deve instanciar um objeto de cada subclasse e exibir as informações e sons correspondentes
'''

from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca:str, modelo:str, ano:int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @abstractmethod
    def exibir_dados(self):
        pass

    @abstractmethod
    def emitir_som(self):
        pass

class Carro(Veiculo):
    def exibir_dados(self):
        print(f'Carro -> Marca: {self.marca} | Modelo: {self.modelo} | Ano: {self.ano}')

    def emitir_som(self):
        print('BUZINA DE CARRO')

class Motocicleta(Veiculo):
    def exibir_dados(self):
        print(f'Moto -> Marca: {self.marca} | Modelo: {self.modelo} | Ano: {self.ano}')

    def emitir_som(self):
        print('BUZINA DE MOTO')

moto_um = Motocicleta('Honda', 'Biz', 2026)
moto_um.exibir_dados()
moto_um.emitir_som()
print(f'\n')

carro_um = Carro('Toyota', 'Corola', 2022)
carro_um.exibir_dados()
carro_um.emitir_som()


