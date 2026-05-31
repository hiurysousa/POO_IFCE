from membro import Membro

class MembroEstudante(Membro):

    def __init__(self, nome, matricula, mensalidade_base, instituicao):
        super().__init__(nome, matricula, mensalidade_base)
        self.instituicao = instituicao

    def calcular_mensalidade(self):
        desconto = self.mensalidade_base * 0.2

        return self.mensalidade_base - desconto
    