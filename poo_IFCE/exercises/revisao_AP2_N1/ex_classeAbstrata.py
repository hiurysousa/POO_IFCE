'''
Uma loja online precisa calcular o frete de suas entregas.
Crie a classe abstrata Frete com os atributos destino e peso, e um método exibir_dados() que exiba essas informações
sem precisar ser sobrescrito. Crie o método abstrato calcular_frete().
Implemente duas subclasses: FreteExpresso, que cobra R$ 15,00 fixos mais R$ 3,50 por kg, e
FreteEconomico, que cobra R$ 5,00 fixos mais R$ 1,20 por kg.
Instancie um objeto de cada, exiba os dados e imprima o valor do frete calculado.
'''
from abc import ABC, abstractmethod

class Frete(ABC):
    def __init__(self, destino:str, peso:float):
        self.destino = destino
        self.peso = peso

    def exibir_dados(self):
        print(f'Destino: {self.destino} | Peso: {self.peso}')

    @abstractmethod
    def calcular_frete(self):
        pass

class FreteExpresso(Frete):

    def calcular_frete(self):
        return 15 + (3.5*self.peso)

class FreteEconomico(Frete):

    def calcular_frete(self):
        return 5 + (1.2*self.peso)

frete_um = FreteExpresso('Aracati', 10)
print(f'Valor do frete {frete_um.calcular_frete()}')
frete_um.exibir_dados()

print(f'\n')

frete_dois = FreteEconomico('Aracati', 10)
print(f'Valor do frete {frete_dois.calcular_frete()}')
frete_dois.exibir_dados()