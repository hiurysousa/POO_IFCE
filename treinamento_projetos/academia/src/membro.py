from abc import ABC, abstractmethod

class Membro(ABC):

    def __init__(self, nome, matricula, mensalidade_base):
        self.nome = nome
        self.matricula = matricula
        self.mensalidade_base = mensalidade_base
        self.historico_treinos = []

    
    @abstractmethod
    def calcular_mensalidade(self):
        pass

    def registrar_treino(self, grupo_muscular):
        if not isinstance(grupo_muscular, str):
            raise TypeError(f'Treino inválido.')
        
        self.historico_treinos.append(grupo_muscular)