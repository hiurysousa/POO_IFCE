'''
Tema: Biblioteca Digital com Agrupamento e Busca por Substring
O Cenário: Você deve criar um sistema que gerencia Livro e Biblioteca. O pulo do gato aqui é que o professor quer que os livros sejam armazenados em um dicionário, agrupados pela categoria, e o método de busca não pode quebrar com espaços extras.

Regras de Negócio e Lógica:

A classe Livro possui: titulo, autor e categoria. Todos os atributos devem ser protegidos com _ e expostos via propriedades de leitura/escrita inline (property).

A classe Biblioteca possui um dicionário privado _acervo onde a chave é o nome da categoria (string) e o valor é uma lista de objetos Livro pertencentes àquela categoria.

Método adicionar_livro(livro): Deve injetar o livro na lista da categoria correta dentro do dicionário. Se a categoria não existir no dicionário ainda, ela deve ser criada dinamicamente.

Método buscar(termo_busca): Deve receber uma string, quebrar em termos, ignorar maiúsculas/minúsculas e retornar uma lista com todos os objetos Livro cujo título ou autor contenham todos os termos pesquisados (igual à lógica de substring com all() que analisamos!). Se a busca for vazia ou cheia de espaços, retorne uma lista vazia.
'''

class Livro:
    def __init__(self, titulo, autor, categoria):
        self._titulo = titulo
        self._autor = autor
        self._categoria = categoria

    @property
    def titulo(self):
        return self._titulo
    
    @property
    def autor(self):
        return self._autor
    
    @property
    def categoria(self):
        return self._categoria
    
class Biblioteca:
    def __init__(self):
        self._acervo = {}


    '''A classe Biblioteca possui um dicionário privado _acervo onde a chave é o nome da categoria (string) e o valor é uma lista de objetos Livro pertencentes àquela categoria. /////
    Método adicionar_livro(livro): Deve injetar o livro na lista da categoria correta dentro do dicionário. Se a categoria não existir no dicionário ainda, ela deve ser criada dinamicamente.'''
    def adicionar_livro(self, livro):
        if not isinstance(livro, Livro):
            raise TypeError(f'Objeto inválido.')
        
        categoria = livro.categoria
        if categoria not in self._acervo:
            self._acervo[categoria] = []

        self._acervo[categoria].append(livro)

    def exibir_livros(self):
        for categoria, lista_livros in self._acervo.items():
            print(f'Categoria: {categoria}')
            
            for livro in lista_livros:
                print(f'Titulo: {livro.titulo} - Autor: {livro.autor}')

livro_um = Livro('Essencialismo', 'Fulano', 'Psicologia')
livro_dois = Livro('Carta ao Pai', 'Franz Kafka', 'Psicologia')
livro_tres = Livro('Helena', 'Machado de Assis', 'Romance')
livro_quatro = Livro('Macbeth', 'Shakespeare', 'Ação')

biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro_um)
biblioteca.adicionar_livro(livro_dois)
biblioteca.adicionar_livro(livro_tres)
biblioteca.adicionar_livro(livro_quatro)


biblioteca.exibir_livros()