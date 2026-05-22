# ✍️ SUA LÓGICA: Crie a classe QuantidadeInvalidaError herdando da classe correta do Python
class QuantidadeInvalidaError(Exception):
    def __init__(self, quantidade):
        self.quantidade = quantidade
        super().__init__(f'Quantidade não permitida: {quantidade}. TRY AGAIN.')
