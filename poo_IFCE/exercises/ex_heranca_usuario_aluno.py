# 1) Em um sistema acadêmico, é necessário modelar diferentes tipos de usuários,
# onde todos compartilham informações básicas, mas possuem características específicas.
#
# Considere a seguinte especificação:
#
#------------------------
# USUARIO
#------------------------
# # nome: str
# # email: str
#------------------------
# + Usuario(nome: str, email: str)
#------------------------
#
#------------------------
# ALUNO
#------------------------
# + matricula: str
# # disciplinas: list
#------------------------
# + Aluno(nome: str, email: str)
#------------------------
#
#------------------------
# PROFESSOR
#------------------------
# # disciplinas_ministradas: list
# # carga_horaria: int
# - salario: float
#------------------------
# + Professor(nome: str, email: str)
#------------------------
#
#------------------------
# COORDENADOR
#------------------------
# # curso: str
# # professores: list
# - bonus: float
#------------------------
# + Coordenador(nome: str, email: str)
#------------------------
#
# Implemente as classes acima em Python, respeitando o uso de herança.
#
# Requisitos:
# 1. As classes Aluno, Professor e Coordenador devem herdar de Usuario.
# 2. Não adicione atributos na classe base que pertencem apenas às subclasses.
# 3. Utilize super() corretamente para inicializar os atributos herdados.
# 4. Inicialize todos os atributos específicos de cada subclasse.
#
# Ao final:
# a) Crie um trecho de código que:
# b) instancie um Aluno, um Professor e um Coordenador;
# c) atribua valores a pelo menos dois atributos específicos de cada objeto;
# d) exiba o nome e o email de cada usuário.

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Aluno(Usuario):
    def __init__(self, nome, email, matricula):
        super().__init__(nome, email)
        self.matricula = matricula
        self._disciplinas = []

class Professor(Usuario):
    def __init__(self, nome, email, carga_horaria, salario):
        super().__init__(nome, email)
        self._disciplinas_ministradas = []
        self._carga_horaria = carga_horaria
        self.__salario = salario

class Coordenador(Usuario):
    def __init__(self, nome, email, curso, bonus):
        super().__init__(nome, email)
        self._curso = curso
        self._professores = []
        self.__bonus = bonus

# --- Execução e Testes ---

aluno_um = Aluno('Hiury', 'hiuryteste@outlook.com', '32452')
aluno_um._disciplinas.append('POO')

professor_um = Professor('Rodrigo', 'rodrigoprof@teste.com', 80, 2400)
professor_um._disciplinas_ministradas.append('Estrutura de Dados')

coordenador_um = Coordenador('Paulo José', 'pjose@outlook.com', 'BCC', 250)
coordenador_um._professores.append('Rodrigo')

faculdade = [aluno_um, professor_um, coordenador_um]

for usuario in faculdade:
    print(f'Nome: {usuario.nome} | Email: {usuario.email}')