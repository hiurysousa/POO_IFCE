'''
Cenário: A empresa cresceu e agora precisamos calcular o salário dos membros da equipe com bônus diferentes
baseados nos seus cargos e regras de negócio.
classDiagram
    class MembroEquipe {
        - nome: String
        - salario_base: float
        + MembroEquipe(nome, salario_base)
        + calcular_salario() float
        + get_nome() String
        + get_salario_base() float
    }

    class Programador {
        - linguagem_principal: String
        + Programador(nome, salario_base, linguagem_principal)
        + calcular_salario() float
    }

    class Gestor {
        - participacao_lucros: float
        + Gestor(nome, salario_base, participacao_lucros)
        + calcular_salario() float
    }
'''
from abc import ABC, abstractmethod
class MembroEquipe(ABC):
    def __init__(self, nome, salario_base):
        self.__nome = nome
        self.salario_base = salario_base
    

    @property
    def nome(self):
        return self.__nome

    @property
    def salario_base(self):
        return self.__salario_base

    @salario_base.setter
    def salario_base(self, salario):
        if salario < 0:
            salario = 1512
        self.__salario_base = salario

    @abstractmethod
    def calcular_salario(self):
        pass


class Programador(MembroEquipe):
    def __init__(self, nome, salario_base, linguagem_principal):
        super().__init__(nome, salario_base)
        self.__linguagem_principal = linguagem_principal

    def calcular_salario(self):
        return self.salario_base*0.1 + self.salario_base
    
    def __str__(self):
        return f'DEV: {self.nome} | Linguagem: {self.__linguagem_principal} | Salário Final: R$ {self.calcular_salario()}'

class Gestor(MembroEquipe):
    def __init__(self, nome, salario_base, participacao_lucros):
        super().__init__(nome, salario_base)
        self.__participacao_lucros = participacao_lucros

    def calcular_salario(self):
        return self.salario_base + self.__participacao_lucros
    
    def __str__(self):
        return f'Gestor: {self.nome} | Salário Final: R$ {self.calcular_salario()}'
    
dev = Programador('Hiury', 3000, 'Python')
chefe = Gestor("Márcio", 5000.00, 1200.00)

print(dev)
print(chefe)
