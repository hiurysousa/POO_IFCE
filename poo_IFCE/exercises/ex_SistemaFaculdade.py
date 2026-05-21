'''
# 7) Sistema acadêmico com especialização

# Modele corretamente a hierarquia:

# Usuario (base)
# Aluno
# Professor
# Coordenador

# Requisitos:
# Aluno deve ter matricula e lista de disciplinas
# Professor deve ter disciplinas ministradas e carga horária
# Coordenador deve ter curso e lista de professores
# Usar super() corretamente
# Evitar repetição de atributos

# Desafio:
# Implemente um método exibir_perfil() polimórfico em cada classe.
'''

from abc import abstractmethod, ABC

class Usuario(ABC):
    def __init__(self, nome, campus):
        self.nome = nome
        self.campus = campus

    @abstractmethod
    def exibir_perfil(self):
        pass


class Aluno(Usuario):
    def __init__(self, nome, campus, matricula):
        super().__init__(nome, campus)
        self.matricula = matricula
        self.disciplinas = []

    def exibir_perfil(self):
        print(f'PERFIL DO USUÁRIO -- Aluno')
        print(f'Nome: {self.nome} | Matricula: {self.matricula} | Campus: {self.campus}')
        print(f'Discipinas do semestre: {self.disciplinas}')


class Professor(Usuario):
    def __init__(self, nome, campus, carga):
        super().__init__(nome, campus)
        self.carga = carga
        self.disciplinas = []

    def exibir_perfil(self):
        print(f'PERFIL DO USUÁRIO -- Professor')
        print(f'Nome: {self.nome} | Carga: {self.carga} | Campus: {self.campus}')
        print(f'Discipinas do semestre: {self.disciplinas}')

class Coordenador(Usuario):
    def __init__(self, nome, campus, curso):
        super().__init__(nome, campus)
        self.curso = curso
        self.professores = []

    def exibir_perfil(self):
        print(f'PERFIL DO USUÁRIO -- Coordenador')
        print(f'Nome: {self.nome} | Curso: {self.curso} | Campus: {self.campus}')
        print(f'Professores do semestre: {self.professores}')

try:
    aluno_um = Aluno('Lucas', 'Quixadá', 202411310)
    aluno_um.disciplinas = ['Estrutura de dados', 'Inglês', 'Física']

    professor_um = Professor('Mario', 'Aracati', 100)
    professor_um.disciplinas = ['Calculo I', 'Calculo II']

    coordenador_um = Coordenador('Pamela', 'Aracati', 'BCC')
    coordenador_um.professores = ['Mario', 'Joao']

    for usuarios in [aluno_um, professor_um, coordenador_um]:
        usuarios.exibir_perfil()
        print(f'\n')
except Exception as e:
    print(f'{e}')


