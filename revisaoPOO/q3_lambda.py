'''
Você tem uma lista de tuplas representando produtos em um carrinho de compras. Cada tupla contém (nome_produto, quantidade, preco_unitario).

Entrada: carrinho = [("Teclado", 2, 150.0), ("Mouse", 1, 80.0), ("Monitor", 1, 900.0)]

Objetivo: Use map e lambda para criar uma lista que contenha apenas o valor total de cada item (quantidade * preço).
'''

carrinho = [("Teclado", 2, 150.0), ("Mouse", 1, 80.0), ("Monitor", 1, 900.0)]


valor_total = list(map(lambda x : x[1] * x[2], carrinho))

print(valor_total)