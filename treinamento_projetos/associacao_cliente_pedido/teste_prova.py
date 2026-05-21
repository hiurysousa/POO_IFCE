class Cliente:
    def __init__(self, cliente_id: int, nome: str):
        self._cliente_id = cliente_id
        self._nome = nome
        self._lista_pedidos = []

    @property
    def id(self):
        return self._cliente_id

    @property
    def nome(self):
        return self._nome

    @property
    def pedidos(self):
        return self._lista_pedidos

    def adicionar_pedido(self, pedido):
        # LÓGICA DE ASSOCIAÇÃO:
        # 1. Verifique se o pedido já NÃO está na lista _pedidos
        # 2. Se não estiver, dê o .append() nele
        # 3. Verifique se o cliente cadastrado dentro desse pedido é diferente de você (self)
        # 4. Se for diferente, chame o método do pedido para definir o cliente atual
        if pedido not in self._lista_pedidos:
            self._lista_pedidos.append(pedido)
            if pedido.cliente != self:
                pedido.definir_cliente(self)


class Pedido:
    def __init__(self, pedido_id: int, valor_total: float):
        self._pedido_id = pedido_id
        self._valor_total = valor_total
        self._cliente = None

    @property
    def id(self):
        return self._pedido_id

    @property
    def valor_total(self):
        return self._valor_total

    @property
    def cliente(self):
        return self._cliente

    def definir_cliente(self, cliente):
        # LÓGICA DE ASSOCIAÇÃO (O QUEBRA-LOOP):
        # 1. Verifique se o cliente recebido é DIFERENTE do _cliente atual
        # 2. Se for diferente, atualize o _cliente privado com o novo cliente
        # 3. Verifique se esse cliente recebido NÃO é nulo (is not None)
        # 4. Se for um cliente real, cheque se este pedido (self) já está na lista de pedidos dele
        # 5. Se não estiver, chame o método do cliente para adicionar este pedido
        if self._cliente != cliente:
            self._cliente = cliente
            if cliente != None:
                if self not in cliente.lista_pedidos:
                    cliente.adicionar_pedido(self)