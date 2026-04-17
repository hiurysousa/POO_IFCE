'''
2. Boletim Escolar (Cálculo de Média)
Cada tupla representa um aluno e suas três notas bimestrais: (Nome, Nota1, Nota2, Nota3).

Entrada: notas = [("Alice", 8, 9, 7), ("Bob", 5, 6, 4), ("Clara", 10, 9, 10)]

Objetivo: Criar uma lista contendo apenas a média aritmética de cada aluno.
'''

notas = [("Alice", 8, 9, 7), ("Bob", 5, 6, 4), ("Clara", 10, 9, 10)]
lista_medias = list(map(lambda x: (x[1] + x[2] + x[3])/3, notas))

for values in lista_medias:
    print(f'{values:.2f}')