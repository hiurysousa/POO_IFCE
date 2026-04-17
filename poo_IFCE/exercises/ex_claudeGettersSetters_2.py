'''
Crie a classe Usuario com os atributos privados __nome e __idade.
Use @property para criar getters para ambos.
Crie um @nome.setter que impeça que o nome seja uma string vazia, e um @idade.setter que impeça idades menores que 0 ou
maiores que 120, lançando ValueError em ambos os casos.
Instancie um objeto, exiba os dados e teste cada proteção com valores inválidos.
'''

class Usuario:

    def __init__(self, nome:str, idade:int):
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @nome.setter
    def nome(self, nome:str):
        if len(nome.strip()) == 0:
            raise ValueError('Resposta vazia.')
        self.__nome = nome

    @idade.setter
    def idade(self, idade:int):
        if idade < 0 or idade > 120:
            raise ValueError('Valor inválido, por favor, acima de 0 e abaixo de 120.')
        self.__idade = idade

usuario_um = Usuario('Hiury', 22)
usuario_dois = Usuario('Clara', 23)
usuario_tres = Usuario('Margarida', 120)

print(f'Nome: {usuario_um.nome} | Idade: {usuario_um.idade}')
print(f'Nome: {usuario_dois.nome} | Idade: {usuario_dois.idade}')
print(f'Nome: {usuario_tres.nome} | Idade: {usuario_tres.idade}')



