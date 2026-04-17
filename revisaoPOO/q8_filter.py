'''

4. Inventário de Loja (Aplicação de Desconto)
Uma lista de produtos contém: (Nome, Preço Original, Categoria).

Entrada: produtos = [("Camisa", 100, "Vestuário"), ("Tênis", 250, "Calçados"), ("Meia", 20, "Vestuário")]

Objetivo: Criar uma lista com os novos preços aplicando um desconto de
10% em todos os itens. (O resultado deve ser apenas os preços com desconto).

'''

produtos = [("Camisa", 100, "Vestuário"), ("Tênis", 250, "Calçados"), ("Meia", 20, "Vestuário")]

produtos_desconto = list(map(lambda x : x[1] - (x[1] * 0.1), produtos))
print(produtos_desconto)