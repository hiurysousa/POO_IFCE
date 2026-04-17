''' 6) Classe de entidade para representar um filme no sistema.
 Atributos: titulo, diretor, duracao e genero. Implemente o construtor.
 Método exibir_info: mostra todos os dados formatados do filme.
 Crie dois objetos de filmes diferentes para testar a classe.
 Avalie se o método exibir_info funciona para ambos os casos.
'''
class Filme:

    def __init__(self, titulo:str, diretor:str, duracao:str, genero:str):
        self.titulo = titulo
        self.diretor = diretor
        self.duracao = duracao
        self.genero = genero

    def exibir_info(self):
        print(f'Filme: {self.titulo} | Diretor: {self.diretor} | Duracao: {self.duracao} | Genero: {self.genero}')

duna = Filme('Duna', 'Diretor_1', '2h:25min', 'Ficção')
saltburn = Filme('Saltburn', 'Diretor_2', '2h', 'Suspense')

duna.exibir_info()
saltburn.exibir_info()