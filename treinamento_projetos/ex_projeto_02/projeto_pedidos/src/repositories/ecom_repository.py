import csv
from src.models.cliente import Cliente
from src.models.pedido import Pedido

class EcomRepository:

    def __init__(self, clientes_path: str, pedidos_path: str):
        self._clientes_path = clientes_path
        self._pedidos_path = pedidos_path
        self._clientes_map = {}  # Guarda {id_do_cliente: objeto_cliente}
        self._pedidos = []       # Lista de objetos Pedido salvos

    def load_data(self):
        # --- PASSO 1: CARREGAR CLIENTES ---
        with open(self._clientes_path, "r", encoding="utf-8") as f:
            leitor = csv.DictReader(f)
            for row in leitor:
                # -------------------------------------------------------------
                # ✍️ SUA LÓGICA AQUI (ISSUE 1 - PARTE A):
                # Tente (try) instanciar Cliente(row["id"], row["nome"], row["email"])
                # Se der certo, guarde no mapa: self._clientes_map[int(row["id"])] = cliente_criado
                # Se der ValueError, ignore o cliente silenciosamente (ou dê um pass)
                # -------------------------------------------------------------
                try:
                    cliente = Cliente(row["id"], row["name"], row["email"])
                    self._clientes_map[int(row["id"])] = cliente
                except ValueError:
                    pass
                

        # --- PASSO 2: CARREGAR PEDIDOS ---
        with open(self._pedidos_path, "r", encoding="utf-8") as f:
            leitor = csv.DictReader(f)
            for row in leitor:
                # -------------------------------------------------------------
                # ✍️ SUA LÓGICA AQUI (ISSUE 1 - PARTE B):
                # 1. Verifique se o int(row["cliente_id"]) existe nas chaves do self._clientes_map
                # 2. Se NÃO existir, capture como erro e printe o dicionário bruto 'row'
                # 3. Se existir, recupere o objeto cliente: cliente_obj = self._clientes_map[id_do_cliente]
                # 4. Abra um bloco 'try' e tente criar o Pedido passando esse 'cliente_obj'
                # 5. Se der certo, adicione em self._pedidos.append(pedido_criado)
                # 6. Se der ValueError (no except), printe a mensagem de erro com a linha bruta
                # -------------------------------------------------------------

                try:
                    id_cliente_pedido = int(row["cliente_id"])
                    if id_cliente_pedido not in self._clientes_map:
                        raise ValueError()
        
                    cliente_objeto = self._clientes_map[id_cliente_pedido]
                    
                    pedido_criado = Pedido(
                        pedido_id=row["id"],
                        cliente_objeto=cliente_objeto,
                        valor_total=row["valor_total"],
                        status=row["status"]
                    )

                    self._pedidos.append(pedido_criado)


                except ValueError:
                    # Se o cliente não existir OU se o construtor do Pedido falhar nas regras:
                    print(f"Pedido inválido ou sem cliente correspondente ignorado: {row}")

        return self._pedidos


        

    def get_pedidos_por_cliente_e_valor(self, busca_cliente: str, valor_minimo: float):
        # -------------------------------------------------------------
        # ✍️ SUA LÓGICA DE BUSCA AQUI (ISSUE 2):
        # 1. Transforme a busca_cliente em minúsculo e dê .split()
        # 2. Crie uma lista vazia de resultados
        # 3. Faça um loop 'for p in self._pedidos:'
        # 4. Pegue as palavras do nome do cliente associado: p.cliente.name.lower().split()
        # 5. Aplique a lógica cumulativa (flag ou all()) para ver se todos os termos estão no nome
        # 6. Garanta também que p.valor_total >= valor_minimo
        # 7. Retorne a lista de resultados válidos
        # -------------------------------------------------------------
        return []