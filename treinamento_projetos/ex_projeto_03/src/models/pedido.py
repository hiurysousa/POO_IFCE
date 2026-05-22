'''
Cliente e Pedido (Associação Bidirecional Controlada): Um cliente tem uma lista de pedidos, e um pedido pertence a um cliente. Eles devem se sincronizar automaticamente, usando as travas de if para evitar o loop infinito.

Pedido e ItemPedido (Agregação): Um pedido funciona como o "carrinho". Ele contém uma lista de itens. Cada ItemPedido guarda o nome do produto, a quantidade e o preço unitário. O pedido deve ser capaz de calcular o seu próprio valor total navegando por essa lista.
'''

from models.item_pedido import ItemPedido

class Pedido:
    def __init__(self, pedido_id: int):
        self.id = pedido_id
        self.cliente = None         # Começa sem cliente
        self.itens = []             # Lista que guardará os objetos ItemPedido

    def adicionar_item(self, item: ItemPedido):
        # ✍️ SUA LÓGICA: Adicione o objeto 'item' na lista self.itens
        if not isinstance(item, ItemPedido):
            raise TypeError(f'Valor inválido.')
        
        self.itens.append(item)

    def calcular_total_pedido(self) -> float:
        # ✍️ SUA LÓGICA COMPLEXA:
        # 1. Calcule a soma bruta de todos os itens usando o loop
        # 2. Se self.cliente for None, retorne a soma bruta pura
        # 3. Se existir um cliente, calcule o desconto chamando o método polimórfico dele:
        # desconto = self.cliente.calcular_desconto_pedido(soma_bruta)
        # 4. Retorne a soma bruta menos o desconto.
        soma = 0
        for item in self.itens:
            soma += item.calcular_subtotal()
        
        if self.cliente == None:
            return soma
        
        return soma - self.cliente.calcular_desconto_pedido(soma)
        

    def definir_cliente(self, cliente_obj):
        # ✍️ SUA LÓGICA (O QUEBRA-LOOP DA ASSOCIAÇÃO):
        # 1. Verifique se o cliente_obj recebido é DIFERENTE do self.cliente atual
        # 2. Se for diferente, mude o self.cliente para o novo objeto
        # 3. Se o cliente_obj não for None, verifique se este pedido (self) 
        #    já está na lista de pedidos dele. Se não estiver, mande o cliente te adicionar.
        if cliente_obj != self.cliente:
            self.cliente = cliente_obj
            if cliente_obj != None:
                if self not in cliente_obj.pedidos:
                    cliente_obj.adicionar_pedido(self)


     