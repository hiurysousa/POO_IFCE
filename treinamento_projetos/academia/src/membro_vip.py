from membro import Membro

class MembroVip(Membro):

    def __init__(self, nome, matricula, mensalidade_base, taxa_personal):
        super().__init__(nome, matricula, mensalidade_base)
        self.taxa_personal = taxa_personal

    def calcular_mensalidade(self):
        
        return self.mensalidade_base + self.taxa_personal