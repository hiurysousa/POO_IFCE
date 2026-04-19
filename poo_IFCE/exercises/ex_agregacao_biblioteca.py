# 4) Em uma aplicação de gerenciamento de biblioteca, é necessário modelar a entidade Biblioteca e a entidade Livro.
# Uma biblioteca **agrega** vários livros, mas cada livro pode existir fora da biblioteca (pode ser transferido ou existir em outras bibliotecas).
# Essa é uma relação de AGREGAÇÃO.

#------------------------
# BIBLIOTECA
#------------------------
# - nome: str
# - endereco: str
# # livros: list[Livro]
#------------------------
# + Biblioteca(nome: str, endereco: str)
# + livros(): list
# + adicionar_livro(livro: Livro)
# + remover_livro(livro: Livro)
#------------------------
class Biblioteca:
    def __init__(self, nome, endereco):
        self.__nome = nome
        self.__endereco = endereco
        self._livros = []

    @property
    def livros(self): 
        return self._livros

    def adicionar_livro(self, livro):
        if livro not in self._livros:
            self._livros.append(livro)

    def remover_livro(self, livro):
        if livro in self._livros:
            self._livros.remove(livro)


#------------------------
# LIVRO
#------------------------
# + titulo: str
# + autor: str
#------------------------
# + Livro(titulo: str, autor: str)
#------------------------

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

# Implemente as classes Biblioteca e Livro em Python, mantendo a agregação entre elas.
# Requisitos:
# 1. A classe Biblioteca deve manter uma lista de livros, sem permitir duplicatas.
# 2. Os livros podem existir fora da biblioteca (não dependem da vida da biblioteca).
# 3. Métodos de adicionar/remover livro devem apenas atualizar a lista da biblioteca.
# 4. Ao final, crie um trecho de código que:
#    a) instancie uma biblioteca e dois livros;
#    b) adicione os livros à biblioteca;
#    c) exiba os títulos dos livros da biblioteca.

biblioteca_um = Biblioteca('Biblioteca Machado de Assis', 'Rua Ze de Alencar, 602')
livro_um = Livro('O Poder do Hábito', 'Fulano')
livro_dois = Livro('Helena', 'Machado de Assis')
biblioteca_um.adicionar_livro(livro_um)
biblioteca_um.adicionar_livro(livro_dois)
for livro in biblioteca_um.livros:
    print(f'Nome do Livro: {livro.titulo}')