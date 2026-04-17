'''
a) adicionar_filme(lista, titulo, genero, ano) — adiciona um novo filme à lista.
b) listar_por_genero(lista, genero) — exibe apenas os filmes do gênero informado.
c) filme_mais_antigo(lista) — retorna o dicionário do filme com menor ano.
d) contar_por_genero(lista) — retorna um dicionário com a contagem de filmes por gênero. Exemplo de retorno esperado:
'''

def adicionar_filme(lista, titulo, genero, ano):
    livro = {'titulo':titulo, 'genero':genero, 'ano':ano}
    lista.append(livro)

    return lista

def listar_por_genero(lista, genero):
    for livros in lista:
        if livros['genero'] == genero:
            print(f'Título: {livros['titulo']} - Gênero: {livros['genero']}')

def filme_mais_antigo(lista):
    menor = lista[0]['ano']
    for filme in filmes:
        if filme['ano'] < menor:
            menor = filme['ano']

    return menor

def contar_por_genero(lista):
    list_generos = []
    for filme in lista:
        list_generos.append(filme['genero'])

    list_generos = list(set(list_generos))

    contagem_genero = {}

    for genero in list_generos:
        qtd = 0
        for filme in lista:
            if filme['genero'] == genero:
                qtd += 1
        contagem_genero[genero] = qtd

    return contagem_genero

filmes = [
    {"titulo": "Matrix",        "genero": "Ficção",  "ano": 1999},
    {"titulo": "Parasita",      "genero": "Drama",   "ano": 2019},
    {"titulo": "Interestelar",  "genero": "Ficção",  "ano": 2014},
    {"titulo": "O Poderoso Chefão", "genero": "Drama", "ano": 1972},
    {"titulo": "Velozes e Furiosos", "genero": "Ação", "ano": 2001},
]

adicionar_filme(filmes, 'Corra', 'Suspense', '2019')
print(f'{contar_por_genero(filmes)}')