'''
O Gemini disse
Excelente escolha. A função sorted() é essencial para quem estuda Engenharia de Dados
ou Programação, e ela brilha de verdade quando usamos o argumento key com uma função lambda.

Aqui estão 3 desafios práticos para você programar:

1. Nível Fácil: Ordenação de Strings por Comprimento
Muitas vezes precisamos ordenar dados não pelo valor alfabético,
mas por alguma característica do dado (como o tamanho).

Entrada: frutas = ["abacaxi", "uva", "morango", "banana", "pera"]

Objetivo: Use a função sorted() e uma lambda para ordenar essa lista da fruta com menos letras para a fruta com mais letras.
'''

frutas = ["abacaxi", "uva", "morango", "banana", "pera"]
frutas_ordenadas = sorted(frutas, key = lambda x : len(x), reverse=False)

print(frutas_ordenadas)