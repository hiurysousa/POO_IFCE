'''
# 26) Cadastro produto:
# Valide preço informado.
# Lance ProdutoInvalido se preço negativo.
# Inclua valor inválido na exceção.
'''

class ProdutoInvalido(Exception):
    def __init__(self, preco):
        super().__init__(f'R$ {preco} É INVÁLIDO. Escreva um número positivo.')

try:
    price = float(input(f'Digite o valor do produto: '))
    if price < 0:
        raise ProdutoInvalido(price)
    print(f'Valor do produto: R${price}')
except ProdutoInvalido as e:
    print(f'{e}')