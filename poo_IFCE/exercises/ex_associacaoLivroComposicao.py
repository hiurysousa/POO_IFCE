class Livro:
    def __init__(self, titulo:str, autor:str):
        self.__titulo = titulo
        self.__autor = autor
        self._capitulos = []

    @property
    def capitulos(self):
        return self._capitulos

    def adicionar_capitulo(self, titulo:str, num_paginas:int):
        novo_capitulo = Capitulo(titulo, num_paginas)
        self._capitulos.append(novo_capitulo)

    def remover_capitulo(self, indice: int):
        """Remove um capítulo com base na sua posição na lista (índice)"""
        if 0 <= indice < len(self._capitulos):
            self._capitulos.pop(indice)
        else:
            print("Erro: Índice de capítulo inválido.")



class Capitulo:
    def __init__(self, titulo:str, num_paginas):
        self.titulo = titulo
        self.num_paginas = num_paginas

livro_um = Livro('Essencialismo','Fulano')
livro_um.adicionar_capitulo('Introdução', 7)
livro_um.adicionar_capitulo('Prefácio', 14)
for capitulo in livro_um.capitulos:
    print(f'titulo: {capitulo.titulo} | paginas: {capitulo.num_paginas}')