'''
Cliente e Pedido (Associação Bidirecional Controlada): Um cliente tem uma lista de pedidos, e um pedido pertence a um cliente. Eles devem se sincronizar automaticamente, usando as travas de if para evitar o loop infinito.

Pedido e ItemPedido (Agregação): Um pedido funciona como o "carrinho". Ele contém uma lista de itens. Cada ItemPedido guarda o nome do produto, a quantidade e o preço unitário. O pedido deve ser capaz de calcular o seu próprio valor total navegando por essa lista.
'''
from models.pedido import Pedido

class Cliente:
    def __init__(self, nome: str):
        self.nome = nome
        self.pedidos = []  # Lista de objetos Pedido

    def adicionar_pedido(self, pedido_obj):
        # ✍️ SUA LÓGICA (O QUEBRA-LOOP DA ASSOCIAÇÃO):
        # 1. Verifique se o pedido_obj já NÃO está na lista self.pedidos
        # 2. Se não estiver, dê o .append() nele
        # 3. Verifique se o cliente cadastrado dentro do pedido_obj é diferente de você (self)
        # 4. Se for diferente, mande o pedido definir você como o cliente dele
        if not isinstance(pedido_obj, Pedido):
            raise TypeError(f'Valor inválido.')
        
        if pedido_obj not in self.pedidos:
            self.pedidos.append(pedido_obj)
            if pedido_obj.cliente != self:
                pedido_obj.definir_cliente(self)

    def calcular_desconto_pedido(self, valor_bruto: float) -> float:
        # Método base que será subscrito (Polimorfismo)
        return 0.0


# ✍️ IMPLEMENTE A CLASSE ClienteRegular HERDANDO DE CLIENTE
# Regra: Se valor_bruto >= 200, desconto é 5% do valor bruto. Se não, é 0.
class ClienteRegular(Cliente):
    def __init__(self, nome: str):
        super().__init__(nome)
        

    def calcular_desconto_pedido(self, valor_bruto: float) -> float:
        if valor_bruto >= 200:
            return valor_bruto * 0.05
        return 0.0


# ✍️ IMPLEMENTE A CLASSE ClienteVIP HERDANDO DE CLIENTE
# Regra: Desconto = 50.0 + (valor_bruto - 50.0) * 0.10
# (Se o valor bruto for menor que 50, o desconto é apenas o valor bruto para não negativar)

class ClienteVIP(Cliente):
    def __init__(self, nome: str):
        super().__init__(nome)
        

    def calcular_desconto_pedido(self, valor_bruto: float) -> float:
        if valor_bruto > 50:
            sobra = valor_bruto - 50 
            return 50 + (sobra * 0.1) 
        
        return valor_bruto