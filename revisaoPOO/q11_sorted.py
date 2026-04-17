'''
2. Nível Médio: Ranking de Notas (Tuplas)
Em sistemas escolares, é comum querer ver quem teve o melhor desempenho.

Entrada: alunos = [("João", 7.5), ("Maria", 9.2), ("Pedro", 6.0), ("Ana", 9.8)]

Objetivo: Ordene a lista de alunos de forma decrescente (do maior para o menor) baseando-se na nota (índice 1 da tupla).
'''

alunos = [("João", 7.5), ("Maria", 9.2), ("Pedro", 6.0), ("Ana", 9.8)]

alunos_ordenados = sorted(alunos, key = lambda x : x[1], reverse=True)

print(alunos_ordenados)