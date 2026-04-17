'''
1. Nível Básico: Estatísticas de Entrada
Peça ao usuário para digitar uma sequência de números separados por espaço (ex: 10 5 20 2).

Objetivo: Converta essa entrada em uma lista de inteiros. Em seguida, utilize as funções len, sum, max e min para exibir: a quantidade de números, a soma total, o maior e o menor valor.

Dica: Use input().split() para obter a lista de strings antes de converter.
'''

user = input('Digite uma lista numérica separada por espaço: ').split()
lista_numerica = []

for num in user:
    num_formatado = int(num)
    lista_numerica.append(num_formatado)

print(f'Tamanho da lista: {len(lista_numerica)} | Soma total: {sum(lista_numerica)} | Maior valor: {max(lista_numerica)} | Menor valor: {min(lista_numerica)}')