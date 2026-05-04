'''
Contexto: Um sistema de cadastro permite apenas usuários maiores de 18 anos. Se tentar cadastrar menor de idade, lança exceção.
Sua tarefa:
Crie a classe MenorDeIdadeError que herda de Exception
Ela deve receber no __init__: nome, idade, idade_minima (que é 18)
Use super().__init__() para gerar uma mensagem que mostre o nome, a idade do usuário e quantos anos faltam
Crie a classe Usuario com:
Atributos: nome, idade, email
Método estático validar_idade(idade, nome) que lança MenorDeIdadeError
O construtor __init__ deve chamar esse método de validação antes de criar o objeto
Teste criando um usuário de 15 anos chamado "Maria"
'''
class MenorDeIdadeError(Exception):
    def __init__(self, nome, idade, idade_minima):
        self.nome = nome
        self.idade = idade
        self.idade_minima = idade_minima
        super().__init__(f'{self.nome} tem {self.idade}, portanto, faltam {idade_minima-self.idade} anos para que possa ser finalizar o cadastramento.')

class Usuario:
    def __init__(self, nome, idade, email):
        Usuario.validar_idade(nome, idade)
        self.nome = nome
        self.idade = idade
        self.email = email
        print(f'Usuari@ cadastrad@ com sucesso!')

    @staticmethod
    def validar_idade(nome, idade):
        if idade < 18:
            raise MenorDeIdadeError(nome, idade, 18)




try:
    user_um = Usuario('Maria', 15, 'maria@teste.com')
except MenorDeIdadeError as e:
    print(f'{e}')
