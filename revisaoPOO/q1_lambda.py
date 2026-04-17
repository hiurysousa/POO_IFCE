"""
Você tem uma lista de preços em Reais (BRL) e precisa convertê-los para Dólares (USD). Considere a taxa de câmbio de 1 USD = 5.00 BRL.

Entrada: precos_brl = [100.0, 250.50, 50.0, 10.0]

Objetivo: Use map e uma função lambda para criar uma nova lista chamada precos_usd.

Dica: A fórmula é valor / 5.0.
"""
precos_brl = [100.0, 250.50, 50.0, 10.0]

precos_usd = list(map(lambda x: x/5.0, precos_brl))
print(f'Os precos {precos_brl} convertido em USD {precos_usd}')
