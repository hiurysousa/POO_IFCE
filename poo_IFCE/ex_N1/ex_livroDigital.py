class LivroDigital:

    def __init__(self, titulo, autor, formato):
        self.titulo = titulo
        self.autor = autor
        self.formato = formato
        self.foi_baixado = False

    def exibir_informacoes(self):
        print(f'Titulo: {self.titulo} | Autor: {self.autor} | Formato: {self.formato}')

    def baixar(self):
        if not self.foi_baixado:
            print(f'O livro {self.titulo} está sendo baixado no formato {self.formato}.')
            self.foi_baixado = True
            print(f'Download concluído com sucesso.')
        else:
            print(f'O livro {self.titulo} já foi baixado anteriormente.')

livro_um = LivroDigital('Essencialismo', 'Fulano', 'PDF')
livro_um.exibir_informacoes()

livro_um.baixar()
livro_um.baixar()

