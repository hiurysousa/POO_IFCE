class Paciente:
    def __init__(self, nome: str, cpf: str):
        # ✍️ SUA LÓGICA DE VALIDAÇÃO:
        # 1. nome e cpf não podem ser vazios (use .strip())
        # 2. cpf deve conter exatamente 9 dígitos numéricos (use .isdigit() e len())
        # *Se falhar:* lance ValueError
        
        if not nome.strip() or not cpf.strip():
            raise ValueError(f'Nome e CPF não podem ser vazios.')
        
        if len(cpf.strip()) != 9:
            raise ValueError(f'Formato de CPF inválido.')


        self._nome = nome
        self._cpf = cpf
        self._consultas_agendadas = [] # Lista de objetos da classe Consulta

    @property
    def nome(self):
        return self._nome


    @property
    def cpf(self):
        return self._cpf
    
    @property 
    def consultas_agendadas(self):
        return self._consultas_agendadas

    # ✍️ IMPLEMENTE:
    # 1. Getters (@property) para name e cpf
    # 2. Getter (@property) para consultas_agendadas