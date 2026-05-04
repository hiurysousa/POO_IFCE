'''
# 25) Sistema e-commerce:
# Verifique carrinho antes de finalizar compra.
# Lance exceção se carrinho vazio.
# Mostre mensagem adequada ao usuário.
'''

class Carrinho:
    def __init__(self, usuario):
        self.nome = usuario
        self.produtos = []

    def adicionar(self, produto, qtd):
        pedido = {'produto':produto, 'quantidade':qtd}
        self.produtos.append(pedido)

    def verificar(self):
        if len(self.produtos) == 0:
            raise ValueError(f'Carrinho vazio, impossível de finalizar a compra.')
        print(f'Compra concluída com sucesso.')
        for itens in self.produtos:
            print(f'{itens}')

try:
    meu_carrinho = Carrinho('Hiury')
    meu_carrinho.adicionar('Carne', 3)
    meu_carrinho.verificar()
except ValueError as e:
    print(f'Erro: {e}')
