# 2) Em um sistema de e-commerce, é necessário calcular o valor final de diferentes tipos de pedidos,
# onde todos compartilham uma estrutura comum, mas possuem regras de cálculo distintas.
#
# Considere a seguinte especificação:
#
#------------------------
# PEDIDO
#------------------------
# # cliente: str
# # valor_base: float
#------------------------
# + Pedido(cliente: str, valor_base: float)
# + total(): float
#------------------------
#
#------------------------
# PEDIDO_NORMAL
#------------------------
#------------------------
# + PedidoNormal(cliente: str, valor_base: float)
# + total(): float
#------------------------
#
#------------------------
# PEDIDO_COM_DESCONTO
#------------------------
# # desconto: float
#------------------------
# + PedidoComDesconto(cliente: str, valor_base: float)
# + total(): float
#------------------------
#
#------------------------
# PEDIDO_EXPRESSO
#------------------------
# # taxa_entrega: float
#------------------------
# + PedidoExpresso(cliente: str, valor_base: float)
# + total(): float
#------------------------
#
# Implemente as classes acima em Python, respeitando o uso de herança e polimorfismo.
#
# Requisitos:
# 1. As classes PedidoNormal, PedidoComDesconto e PedidoExpresso devem herdar de Pedido.
# 2. O método total() deve ser implementado na classe base e sobrescrito nas subclasses.
# 3. Cada subclasse deve aplicar sua própria regra:
#    - PedidoNormal: retorna apenas o valor_base.
#    - PedidoComDesconto: retorna valor_base com desconto aplicado.
#    - PedidoExpresso: retorna valor_base acrescido da taxa de entrega.
# 4. Utilize super() para inicializar os atributos herdados.
#
# Ao final:
# a) Crie um trecho de código que:
# b) instancie um objeto de cada tipo de pedido;
# c) armazene-os em uma lista;
# d) percorra a lista e exiba o valor total de cada pedido utilizando o método total().

class Pedido:
    def __init__(self, cliente, valor_base):
        self._cliente = cliente
        self._valor_base = valor_base

    def total(self):
        return self._valor_base

class Pedido_Normal(Pedido):
    def __init__(self, cliente, valor_base):
        super().__init__(cliente, valor_base)

    def total(self):
        return super().total()

class Pedido_Desconto(Pedido):
    def __init__(self, cliente, valor_base):
        super().__init__(cliente, valor_base)
        self._desconto = 0

    def total(self):
        return super().total() - self._desconto

class Pedido_Expresso(Pedido):
    def __init__(self, cliente, valor_base):
        super().__init__(cliente, valor_base)
        self._taxa_entrega = 0

    def total(self):
        return super().total() + self._taxa_entrega

# --- Execução e Testes ---

pedido_normal = Pedido_Normal('Hiury', 75)

pedido_desconto = Pedido_Desconto('Clara', 105)
pedido_desconto._desconto = 10

pedido_expresso = Pedido_Expresso('Marcia', 200)
pedido_expresso._taxa_entrega = 15

# Demonstração de Polimorfismo
pedidos = [pedido_normal, pedido_desconto, pedido_expresso]

for pedido in pedidos:
    print(f'Cliente: {pedido._cliente} | Total do pedido: R$ {pedido.total():.2f}')