'''
3. Nível Difícil: Ordenação de Dicionários (Logs de Sistema)
Imagine que você está processando dados de um banco de dados ou API que vieram como uma lista de dicionários. Cada dicionário representa um produto em estoque.

Entrada:

Python
estoque = [
    {"produto": "Teclado", "preco": 150, "quantidade": 45},
    {"produto": "Mouse", "preco": 80, "quantidade": 120},
    {"produto": "Monitor", "preco": 900, "quantidade": 10},
    {"produto": "Headset", "preco": 250, "quantidade": 5}
]
Objetivo: Ordene o estoque pelo valor total investido em cada produto (Preço × Quantidade). O resultado deve mostrar os produtos com o maior capital investido primeiro.
'''

estoque = [
    {"produto": "Teclado", "preco": 150, "quantidade": 45},
    {"produto": "Mouse", "preco": 80, "quantidade": 120},
    {"produto": "Monitor", "preco": 900, "quantidade": 10},
    {"produto": "Headset", "preco": 250, "quantidade": 5}
]

estoque_ordenado = sorted(estoque, key = lambda x: x["preco"] * x["quantidade"], reverse=True)
estoque_formatado = list(map(lambda x : f'{x["produto"]}: R${x["preco"] * x["quantidade"]}', estoque_ordenado))
print(estoque_formatado)