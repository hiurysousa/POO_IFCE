'''
# 22) Sistema vendas:
# Leia preço do produto via input.
# Converta para float.
# Trate ValueError com mensagem clara.
'''

try:
    price = float(input('Valor do produto: '))

    print(f'Preço do produto: {price}')
except ValueError as e:
    print(f'Erro na conversão: {e}')
    print(f'Please, try again.')