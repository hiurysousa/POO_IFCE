from models.cliente import Cliente, ClienteRegular, ClienteVIP
from models.pedido import Pedido
from models.item_pedido import ItemPedido
from errors.ecommerce_errors import QuantidadeInvalidaError

def main():
    print("=== EXECUTANDO O DESAFIO SUPREMO ===")

    # -------------------------------------------------------------
    # TESTE 1: Exceção Personalizada
    # -------------------------------------------------------------
    try:
        print("\nTentando criar item com quantidade inválida...")
        item_com_erro = ItemPedido("Cabo HDMI", 0, 25.0)
        print("❌ FALHA: O sistema aceitou quantidade zero!")
        assert False
    except QuantidadeInvalidaError as e:
        print(f"🟢 SUCESSO: Exceção customizada disparada corretamente: {e}")

    # -------------------------------------------------------------
    # TESTE 2: Polimorfismo com Cliente Regular
    # -------------------------------------------------------------
    print("\nTestando Pedido com Cliente Regular...")
    item1 = ItemPedido("Teclado", 1, 100.0)
    item2 = ItemPedido("Mouse", 1, 100.0) # Bruto total: 200.0
    
    pedido_regular = Pedido(101)
    pedido_regular.adicionar_item(item1)
    pedido_regular.adicionar_item(item2)
    
    cliente_regular = ClienteRegular("João Silva")
    cliente_regular.adicionar_pedido(pedido_regular)
    
    # Cliente Regular: Compra de 200 reais ganha 5% de desconto (10 reais). Líquido: 190.0
    assert pedido_regular.calcular_total_pedido() == 190.0, f"Erro regular: {pedido_regular.calcular_total_pedido()}"
    print("🟢 SUCESSO: Desconto do Cliente Regular aplicado corretamente (R$ 190.0)!")

    # -------------------------------------------------------------
    # TESTE 3: Polimorfismo com Cliente VIP
    # -------------------------------------------------------------
    print("\nTestando Pedido com Cliente VIP...")
    pedido_vip = Pedido(102)
    pedido_vip.adicionar_item(ItemPedido("Monitor Ultrawide", 1, 1050.0)) # Bruto: 1050.0
    
    clientevip = ClienteVIP("Hiury VIP")
    clientevip.adicionar_pedido(pedido_vip)
    
    # Cliente VIP: 1050 bruto -> tira 50 fixo (sobra 1000) -> 10% de 1000 é 100.
    # Desconto total = 50 + 100 = 150. Valor líquido: 1050 - 150 = 900.0
    assert pedido_vip.calcular_total_pedido() == 900.0, f"Erro VIP: {pedido_vip.calcular_total_pedido()}"
    print("🟢 SUCESSO: Desconto do Cliente VIP aplicado corretamente (R$ 900.0)!")

    print("\n🏆 SENSACIONAL! Você destruiu o último chefão de POO. Nota 10 garantida!")

if __name__ == "__main__":
    main()