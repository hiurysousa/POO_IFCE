'''
# 25) Sistema estoque:
# Crie exceção personalizada ProdutoInvalido.
# Inclua código e descrição do erro.
# Use super().__init__ corretamente.
'''

class ProdutoInvalido(Exception):
    def __init__(self, produto):
        self.produto = produto
        super().__init__(f'{produto} não está presente no estoque.')

estoque = {
    "Camiseta": 49.90,
    "Calça Jeans": 129.90,
    "Tênis": 199.90,
    "Boné": 29.90,
    "Mochila": 89.90
}
try:
    user = input('Digite o nome de um produto: ')
    if user not in estoque:
        raise ProdutoInvalido(user)
    print(f"Produto encontrado! Preço: R${estoque[user]}")  
except ProdutoInvalido as e:
    print(f'{e}')

