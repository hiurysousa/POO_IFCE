'''
Você foi designado para criar o módulo de cadastro de colaboradores de uma empresa de software.
O objetivo é garantir que nenhum membro seja registrado com dados inválidos ou inconsistentes.
class MembroEquipe {
        - nome: String
        - idade: int
        - cpf: String
        - cargo: String
        + MembroEquipe(nome, idade, cpf, cargo)
        + get_nome() String
        + set_nome(novo_nome) void
        + get_idade() int
        + set_idade(nova_idade) void
        + get_cpf() String
        + get_cargo() String
    }
'''

class MembroEquipe:
    def __init__(self, nome, idade, cpf, cargo):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf
        self.cargo = cargo

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def cpf(self):
        return self.__cpf

    @property
    def cargo(self):
        return self.__cargo

    @nome.setter
    def nome(self, novo_nome):
        MembroEquipe.valida_nome(novo_nome)
        self.__nome = novo_nome

    @idade.setter
    def idade(self, nova_idade):
        if 18 < nova_idade < 75:
            self.__idade = nova_idade
        else:
            raise ValueError(f'Idade não permitida.')

    @cargo.setter
    def cargo(self, cargo):
        if cargo not in ['Dev', 'Design', 'Testes', 'Gestão']:
            self.__cargo = 'Estagiário'
        else:
            self.__cargo = cargo

    @staticmethod
    def valida_nome(nome):
        if len(nome) < 3:
            raise ValueError(f'Nome Inválido.')

    @staticmethod
    def valida_cpf(cpf):
        if len(cpf) != 11 or cpf.isnumeric() == False:
            raise ValueError(f'CPF Inválido.')

    def __str__(self):
        return f'{self.__cargo} Nome: {self.__nome} | CPF: {self.__cpf} | Status: Verificado'


membro_um = MembroEquipe('Hiury', 23, '00088855560', 'testando')
print(membro_um)