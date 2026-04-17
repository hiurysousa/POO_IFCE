'''
Uma escola precisa de um sistema para gerenciar seus funcionários.
Todo funcionário possui nome e salário base. Existem dois tipos: professor e coordenador.
A classe base deve se chamar Funcionario e as derivadas Professor e Coordenador.
Crie o método exibir_dados() na classe base sem precisar ser sobrescrito.
Crie o método calcular_salario_final() como abstrato,
onde o Professor recebe um bônus de 10% sobre o salário base e o Coordenador recebe 25%.
Instancie um objeto de cada subclasse, exiba os dados e imprima o salário final calculado.
'''

from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome:str, salario:float):
        self.nome = nome
        self._salario = salario

    def exibir_dados(self):
        print(f'Nome: {self.nome} || Salário: {self.salario}')

    @abstractmethod
    def calcular_salario_final(self):
        pass

class Professor(Funcionario):
    def calcular_salario_final(self):
        return (self._salario * 0.10) + self._salario

class Coordenador(Funcionario):
    def calcular_salario_final(self):
        return (self._salario * 0.25) + self._salario

funcionario_um = Professor('Paulo', 2000)
print(f'Salario do {funcionario_um.nome} = R$ {funcionario_um.calcular_salario_final()}')

coordenador_um = Coordenador('Maria', 5000)
print(f'Salario da {coordenador_um.nome} = R$ {coordenador_um.calcular_salario_final()}')