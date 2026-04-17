import rich
class Livro:
    def __init__(self, titulo = None, paginas = 0):
        self.titulo = titulo
        self.paginas = paginas

    def avancarPaginas(self, paginas = 0):
        if paginas >= self.paginas:
            print(f'Você finalizou o livro.')
        else:
            print(f'Você avançou {paginas} páginas.')
            self.paginas -= paginas
            print(f'Você está na página {self.paginas} ')

    def __str__(self):
        return f'Livro: {self.titulo} | Quantidade de folhas: {self.paginas}'

l1 = Livro("Rápido e Devagar", 605)
print(l1)
l1.avancarPaginas(5)
rich.inspect(l1)