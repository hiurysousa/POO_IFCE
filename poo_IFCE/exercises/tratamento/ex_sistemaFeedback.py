'''
# 28) Sistema feedback:
# Leia mensagem do usuário do teclado.
# Salve em arquivo usando try-finally.
# Garanta fechamento do arquivo sempre.
'''



'''try:
    arquivo = open("messagem.txt", "a")
    arquivo.write(mensagem)
finally:
    if arquivo:
        arquivo.close()'''
class ProdutoInvalido(Exception):
    def __init__(self, preco):
        super().__init__(f'R$ {preco} EH INVALIDO. Escreva um numero positivo.')

try:
    price = float(input(f'Digite o valor do produto: '))
    if price < 0:
        raise ProdutoInvalido(price)
    print(f'Valor do produto: R${price}')
except ProdutoInvalido as e:
    with open('mensagem_erro2.txt', 'w') as arquivo:
        arquivo.write(str(e))


