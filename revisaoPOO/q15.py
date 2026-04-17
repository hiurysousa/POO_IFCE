'''
2. Nível Médio: Processamento com Map e Round
Você tem uma lista de preços de produtos em dólar: precos_usd = [19.99, 5.50, 125.0, 49.90].

Objetivo: Use a função map com uma lambda para converter esses preços para Real (multiplique por 5.0). No final, use round para deixar cada valor com apenas 2 casas decimais.
'''

precos_usd = [19.99, 5.50, 125.0, 49.90]
precos_convertidos = list(map(lambda x : f'{round(x * 5.0, 2)}', precos_usd))

print(precos_convertidos)