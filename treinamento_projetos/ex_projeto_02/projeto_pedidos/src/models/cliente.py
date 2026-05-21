class Cliente:
    def __init__(self, cliente_id: int, nome: str, email: str):
        # -------------------------------------------------------------
        # ✍️ SUA LÓGICA DE VALIDAÇÃO AQUI (ISSUE 1):
        # 1. Converta o cliente_id para int. Se for <= 0, lance ValueError
        # 2. Limpe o nome e o email usando .strip()
        # 3. Se o nome limpo ou email limpo forem vazios, lance ValueError
        # 4. Se o email não contiver "@", lance ValueError
        # -------------------------------------------------------------
        
        # Se passar nas validações, salve nos atributos privados:
        id_formatado = int(cliente_id)

        if id_formatado <= 0 or not id_formatado:
            raise ValueError(f'ID precisa ser inteiro e maior que 0.')
        
        if not nome.strip() or not email.strip():
            raise ValueError(f'Nome e email não podem ser vazios.')
        
        if '@' not in email:
            raise ValueError(f'Email inválido.')


        self._id = id_formatado
        self._nome = nome.strip()
        self._email = email.strip()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._nome

    @property
    def email(self):
        return self._email

    def __repr__(self):
        return f"Cliente(id={self._id}, nome='{self._nome}', email='{self._email}')"