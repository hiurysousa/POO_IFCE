'''
Contexto: Uma loja tem um sistema de estoque. Ao tentar vender um produto, se a quantidade for maior que a disponível,
deve lançar uma exceção personalizada.
Sua tarefa:
Crie a classe EstoqueInsuficienteError que herda de Exception
Ela deve receber no __init__: nome_produto, disponivel, solicitado
Use super().__init__() para gerar uma mensagem clara
Crie a classe Produto com:
Atributos: nome, preco, quantidade_estoque
Método vender(quantidade) que lança EstoqueInsuficienteError se necessário
Teste criando um produto com 3 unidades e tentando vender 10
'''
class EstoqueInsuficienteError(Exception):
    def __init__(self, nome, disponivel, solicitado):
        self.nome = nome
        self.disponivel = disponivel
        self.solicitado = solicitado
        super().__init__(f'Impossivel realizar a venda, estoque {disponivel} menor que o solicitado ({solicitado}).')

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def vender(self, qtd):
        if self.quantidade < qtd:
            raise EstoqueInsuficienteError(self.nome, self.quantidade, qtd)
        self.quantidade -= qtd

try:
    produto_um = Produto('Arroz', 5.0, 10)
    produto_um.vender(15)
except EstoqueInsuficienteError as e:
    print(f'{e}')