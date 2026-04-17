'''
Desafio: Prioridade de Entrega
Você recebeu uma lista de pedidos pendentes. Cada dicionário contém o nome do cliente, a distância da entrega (em km) e o valor total da compra.

O seu objetivo é ordenar essa lista para que o entregador saiba qual fazer primeiro. A regra de negócio é: Priorize quem está mais perto (distância menor). Se houver empate na distância, o critério de desempate deve ser o maior valor da compra.

Entrada:
Python
pedidos = [
    {"cliente": "Alice", "distancia": 10, "valor": 150.0},
    {"cliente": "Bruno", "distancia": 5, "valor": 80.0},
    {"cliente": "Carla", "distancia": 10, "valor": 300.0},
    {"cliente": "Diego", "distancia": 2, "valor": 50.0}
]
'''
pedidos = [
    {"cliente": "Alice", "distancia": 10, "valor": 150.0},
    {"cliente": "Bruno", "distancia": 5, "valor": 80.0},
    {"cliente": "Carla", "distancia": 10, "valor": 300.0},
    {"cliente": "Diego", "distancia": 2, "valor": 50.0}
]

pedidos_ordenados = sorted(pedidos, key = lambda x : (x["distancia"], x["valor"]), reverse=True)
pedidos_formatados = list(map(lambda x : f'Cliente: {x['cliente']} | Distância: {x['distancia']}', pedidos_ordenados))
print(pedidos_formatados)