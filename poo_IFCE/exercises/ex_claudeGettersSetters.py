'''
Crie a classe Produto com o atributo privado __preco.
Use @property para criar um getter para preco.
Crie um @preco.setter que impeça que o preço seja definido como zero ou negativo, lançando um ValueError caso isso ocorra.
Instancie um objeto da classe, exiba o preço e tente atribuir um valor inválido para testar a proteção.
'''

class Produto:

    def __init__(self, preco:float):
        self.preco = preco

    @property
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    def preco(self, valor:float):
        if valor <= 0:
            raise ValueError('Valor passado como parâmetro é igual ou abaixo de 0.')
        self.__preco = valor

produto_um = Produto(150)


print(f'O preço do produto é R$ {produto_um.preco}')

