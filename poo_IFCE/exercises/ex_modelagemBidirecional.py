'''
# 8) Modelagem com associação
# Modele as classes Aluno e Curso com associação:
# Um aluno pode estar em vários cursos
# Um curso pode ter vários alunos

# Requisitos:
# evitar duplicatas
# manter consistência bidirecional
# métodos:
# Aluno.adicionar_curso()
# Curso.adicionar_aluno()

# Teste:
# crie 2 alunos e 2 cursos
# associe cruzadamente
# exiba os relacionamentos
'''

class Aluno:
    def __init__(self, nome_aluno):
        self.nome = nome_aluno
        self.cursos = []

    def adicionar_curso(self, curso):
        if curso not in self.cursos:
            self.cursos.append(curso)

        if self not in curso.alunos:
            curso.adicionar_aluno(self)


class Curso:
    def __init__(self, nome_curso):
        self.nome = nome_curso
        self.alunos = []

    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos:
            self.alunos.append(aluno)

        if self not in aluno.cursos:
            aluno.adicionar_curso(self)

aluno_um = Aluno('Joao')
aluno_dois = Aluno('Kamille')

curso_um = Curso('BCC')
curso_dois = Curso('Eventos')

aluno_um.adicionar_curso(curso_um)
curso_um.adicionar_aluno(aluno_dois)

for aluno in curso_um.alunos:
    print(f'{aluno.nome}')