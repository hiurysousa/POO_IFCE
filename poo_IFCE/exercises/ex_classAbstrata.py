from abc import ABC, abstractmethod

class Veiculo(ABC):

    def __init__(self, marca:str, modelo:str, ano:int) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @abstractmethod
    def definir_marca(self, marca:str) -> None:
        pass

    @abstractmethod
    def definir_modelo(self, modelo:str) -> None:
        pass

    @abstractmethod
    def exibir_informacoes(self) -> None:
        pass

class Sedan(Veiculo):
    def definir_marca(self, marca: str) -> None:
        self.marca = marca

    def definir_modelo(self, modelo: str) -> None:
        self.modelo = modelo


    def exibir_informacoes(self) -> None:
        print(f'INFO - Veículo:')
        print(f'Marca: {self.marca} | Modelo: {self.modelo} | Ano: {self.ano}')

v1 = Sedan('Honda', 'Civic', 2010)
v1.exibir_informacoes()
