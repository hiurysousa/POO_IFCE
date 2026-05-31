from membro import Membro

class UnidadeAcademia:

    def __init__(self, nome_filial):
        self.nome_filial = nome_filial
        self.membros = []

    def matricular_membro(self, membro):
        if not isinstance(membro, Membro):
            raise TypeError(f'Objeto inválido.')
    
        self.membros.append(membro)

    def faturamento_total(self):
        soma = 0
        for membro in self.membros:
            soma += membro.calcular_mensalidade()

        return soma
    
