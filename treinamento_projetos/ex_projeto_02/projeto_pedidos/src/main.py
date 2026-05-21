from src.repositories.ecom_repository import EcomRepository

def main():
    repo = EcomRepository("data/clientes.csv", "data/pedidos.csv")
    
    print("=== CARREGANDO DADOS E EXIBINDO LOGS DE ERRO ===")
    pedidos_carregados = repo.load_data()
    
    print("\n=== PEDIDOS CARREGADOS COM SUCESSO NO SISTEMA ===")
    for p in pedidos_carregados:
        print(p)
        
    print("\n=== TESTANDO BUSCA DA ISSUE 2 (Exemplo: cliente 'silva' e valor min: 100) ===")
    resultados = repo.get_pedidos_por_cliente_e_valor("silva", 100.0)
    for r in resultados:
        print(r)

if __name__ == "__main__":
    main()