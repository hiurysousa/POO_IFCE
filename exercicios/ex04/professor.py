from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'{self.nome} acabou de começar a aula.')

    def estudar(self):
        print(f'{self.nome} está estudando especialização fora do país.')