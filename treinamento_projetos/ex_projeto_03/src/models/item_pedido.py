'''
Cliente e Pedido (Associação Bidirecional Controlada): Um cliente tem uma lista de pedidos, e um pedido pertence a um cliente. Eles devem se sincronizar automaticamente, usando as travas de if para evitar o loop infinito.

Pedido e ItemPedido (Agregação): Um pedido funciona como o "carrinho". Ele contém uma lista de itens. Cada ItemPedido guarda o nome do produto, a quantidade e o preço unitário. O pedido deve ser capaz de calcular o seu próprio valor total navegando por essa lista.
'''

from errors.ecommerce_errors import QuantidadeInvalidaError

class ItemPedido:
    def __init__(self, produto: str, quantidade: int, preco_unitario: float):
        # Atributos públicos normais (mínimo absoluto para o teste)
        # ✍️ SUA LÓGICA: Se quantidade for <= 0, lance QuantidadeInvalidaError com uma mensagem
        if quantidade <= 0:
            raise QuantidadeInvalidaError(quantidade)
        
        self.produto = produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def calcular_subtotal(self) -> float:
        # ✍️ SUA LÓGICA: Retorne a quantidade multiplicada pelo preço unitário
        

        return self.quantidade * self.preco_unitario