class PedidoService:

    def __init__(self):
        self.minha_lista = []

    def adicionar_pedido(self, numero, cliente, valor):
        self.minha_lista.append({'numero':numero, 'cliente':cliente, 'valor':valor})
        return self.minha_lista

    def listar_pedidos(self):
        for pedido in self.minha_lista:
            print(f'Numero: {pedido["numero"]}')
            print(f'Cliente: {pedido["cliente"]}')
            print(f'Valor: R${pedido["valor"]}')

    def calcular_total(self):
        total = 0
        for pedido in self.minha_lista:
            total += pedido['valor']

        return total

service = PedidoService()
service.adicionar_pedido('1010','Hiury', 1500)

service.adicionar_pedido('1020','Clara',320)

service.adicionar_pedido('1030','Ryan',100)

service.listar_pedidos()
valor_soma = service.calcular_total()
print(f'\nA soma total dos valores é: {valor_soma}')