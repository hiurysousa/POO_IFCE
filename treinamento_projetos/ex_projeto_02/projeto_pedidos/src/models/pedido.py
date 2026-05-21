from src.models.cliente import Cliente

class Pedido:
    def __init__(self, pedido_id: int, cliente_objeto: Cliente, valor_total: float, status: str):
        # -------------------------------------------------------------
        # ✍️ SUA LÓGICA DE VALIDAÇÃO AQUI (ISSUE 1):
        # 1. Converta o pedido_id para int. Se for <= 0, lance ValueError
        # 2. Valide se cliente_objeto é REALMENTE da classe Cliente:
        #    use: if not isinstance(cliente_objeto, Cliente): lance ValueError
        # 3. Converta valor_total para float. Se for < 0, lance ValueError
        # 4. Trate o status: limpe com .strip(). Se for diferente de 'Pago' e 
        #    diferente de 'Pendente', force a variável a ser 'Pendente'
        # -------------------------------------------------------------


        id_formatado = int(pedido_id)
        valor_formatado = float(valor_total)

        if id_formatado <= 0 or not id_formatado:
            raise ValueError(f'ID precisa ser inteiro e positivo.')
        
        if not isinstance(cliente_objeto, Cliente):
            raise ValueError(f'Cliente/Objeto inválido.')

        if valor_formatado < 0:
            raise ValueError(f'Valor total inválido.')
        
        if status not in ["Pendente", "Pago"]:
            status = "Pendente"

        self._id = id_formatado
        self._cliente = cliente_objeto
        self._valor_total = valor_formatado
        self._status = status  # Deve salvar apenas 'Pago' ou 'Pendente'

    @property
    def id(self):
        return self._id

    @property
    def cliente(self):
        return self._cliente

    @property
    def valor_total(self):
        return self._valor_total

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, novo_status: str):
        # Permite alterar o status depois, desde que seja 'Pago' ou 'Pendente'
        if novo_status in ['Pago', 'Pendente']:
            self._status = novo_status

    def __repr__(self):
        return f"Pedido(id={self._id}, cliente='{self._cliente.name}', valor={self._valor_total}, status='{self._status}')"