'''
Crie a classe Estoque com os atributos privados __produto e __quantidade.
Use @property para criar getters para ambos.
Crie um @quantidade.setter que impeça que a quantidade seja negativa, lançando um ValueError.
Crie também um método adicionar() que some uma quantidade ao estoque e um método remover() que subtraia,
impedindo que o estoque fique abaixo de zero. Instancie um objeto, teste as operações e tente provocar os erros.
'''

class Estoque:

    def __init__(self, produto:str, quantidade:int):
        self.produto = produto
        self.quantidade = quantidade

    @property
    def produto(self):
        return self.__produto

    @property
    def quantidade(self):
        return self.__quantidade

    @produto.setter
    def produto(self, produto:str):
        self.__produto = produto

    @quantidade.setter
    def quantidade(self, qtd:int):
        if qtd < 0:
            raise ValueError('Quantidade não pode ser negativa.')
        self.__quantidade = qtd

    def adicionar(self, adicional:int):
        self.__quantidade += adicional

    def remover(self, qtd_remove:int):
        if qtd_remove > self.__quantidade:
            raise ValueError(f'Impossível remover mais do que contém no estoque.')
        self.quantidade = self.__quantidade - qtd_remove

feijao = Estoque('Carioca', 50)
feijao.adicionar(25)
feijao.remover(10)
print(f'Produto: {feijao.produto} | Quantidade: {feijao.quantidade}')

arroz = Estoque('Branco', 100)
arroz.remover(101)
print(f'Produto: {arroz.produto} | Quantidade: {arroz.quantidade}')
