import rich
class Fornecedor:

    def __init__(self, nome:str, cnpj:str):
        self.nome = nome
        self.cnpj = cnpj
        self._produtos = []

    @property
    def produtos(self):
        return self._produtos

    def adicionar_produto(self, produto):
        if produto not in self._produtos:
            self._produtos.append(produto)

            if produto.fornecedor != self:
                produto.definir_fornecedor(self)

    def remover_produto(self, produto):
        if produto in self._produtos:
            self._produtos.remove(produto)

            if produto.fornecedor == self:
                produto.definir_fornecedor(None)


class Produto:
    def __init__(self, nome:str, preco:float):
        self.nome = nome
        self.preco = preco
        self._fornecedor = None

    @property
    def fornecedor(self):
        return self._fornecedor

    def definir_fornecedor(self, fornecedor):
        if not isinstance(fornecedor, Fornecedor):
            raise TypeError('Não é fornecedor válido.')

        self._fornecedor = fornecedor
        if self not in fornecedor.produtos:
            fornecedor.adicionar_produto(self)

f1 = Fornecedor('Dois irmãos', '000111222333')
p1 = Produto('Carne Moída', 25.5)
p2 = Produto('Arroz', 4.5)

p1.definir_fornecedor(f1)
f1.adicionar_produto(p2)

print(f'Fornecedor: {f1.nome}')
for produto in f1.produtos:
    print(f'Produto: {produto.nome} || Fornecedor: {produto.fornecedor.nome}')


