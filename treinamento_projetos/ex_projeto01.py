'''
Projeto 1 - Cadastro Consistente
Contexto:
Você precisa desenvolver um sistema de cadastro de usuários para uma plataforma online.
O sistema deve garantir que apenas dados válidos sejam armazenados, utilizando os conceitos de encapsulamento,
validação no construtor e exceções personalizadas.

Requisitos:

Crie uma classe Usuario com os seguintes atributos privados: _nome, _email, _idade

Crie a classe DadosInvalidosError que herda de Exception. Esta exceção deve ser lançada sempre que algum dado de cadastro for inválido.

Implemente um construtor que recebe nome, email e idade. O construtor deve validar todos os dados antes
de atribuí-los aos atributos privados. Se qualquer validação falhar, lance a exceção DadosInvalidosError
com uma mensagem específica sobre qual campo está inválido.

Regras de validação:
O nome deve ter pelo menos 3 caracteres e não pode estar vazio.
O email deve conter o símbolo @ e um ponto . após o @.
A idade deve ser um número inteiro entre 0 e 120.

Crie métodos getters públicos para acessar cada atributo privado (get_nome, get_email, get_idade).

Crie um método setter para a idade (set_idade) que permita alterar a idade do usuário após o cadastro,
mas que também aplique a mesma validação.

Crie um método exibir_dados que retorne uma string formatada com todas as informações do usuário.

Cenários de teste que você deve implementar após criar a classe:
Teste 1: Tente cadastrar um usuário com nome vazio, email "joaoemail.com" e idade 25. O sistema deve lançar exceção.
Teste 2: Tente cadastrar um usuário com nome "Maria", email "maria@email" (sem ponto após o @) e idade 150. O sistema deve lançar exceção.
Teste 3: Cadastre um usuário válido com seus dados. Em seguida, exiba os dados usando o método exibir_dados.
Teste 4: Altere a idade do usuário válido para 25 anos usando o setter. Mostre os dados atualizados.
Teste 5: Tente alterar a idade para 130 anos. O sistema deve lançar exceção e manter a idade original.
'''

class DadosInvalidosError(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class Usuario:
    def __init__(self, nome, email, idade):
        Usuario.valida_nome(nome)
        Usuario.valida_email(email)
        Usuario.valida_idade(idade)

        self._nome = nome
        self._email = email
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def email(self):
        return self._email

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        Usuario.valida_idade(nova_idade)
        self._idade = nova_idade

    @staticmethod
    def valida_nome(nome):
        if len(nome) < 3:
            raise DadosInvalidosError(f'Nome: {nome} inválido. Escreva um nome com no mínimo 3 caracteres.')

    @staticmethod
    def valida_email(email):
        if "@" not in email or "." not in email.split("@")[-1]:
            raise DadosInvalidosError(f'Email: {email} inválido. Digite um email válido para prosseguir.')

    @staticmethod
    def valida_idade(idade):
        if idade < 0 or idade > 120:
            raise DadosInvalidosError(f'Idade: {idade} inválida. Escreva uma idade correta.')

    def exibir_dados(self):
        print(f'| DADOS DO USUÁRIO |')
        print(f'Nome: {self._nome} - Email: {self._email} - Idade: {self._idade} anos.')


try:
    usuario_um = Usuario("", "joaoemail.com", 25)
except DadosInvalidosError as e:
    print(f"Teste 1: {e}")

try:
    usuario_dois = Usuario("Maria", "maria@email", 150)
except DadosInvalidosError as e:
    print(f"Teste 2: {e}")

try:
    usuario_tres = Usuario("Endrick", "endrick@teste.com", 17)
    print("Teste 3 - Antes da alteração:")
    usuario_tres.exibir_dados()

    usuario_tres.idade = 25
    print("\nTeste 4 - Após alterar para 25:")
    usuario_tres.exibir_dados()

    usuario_tres.idade = 130
except DadosInvalidosError as e:
    print(f"\nTeste 5: {e}")
    print("Idade permanece:", usuario_tres.idade)
