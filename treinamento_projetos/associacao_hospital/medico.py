class Medico:
    def __init__(self, nome: str, crm: str, especialidade: str):
        # ✍️ SUA LÓGICA DE VALIDAÇÃO:
        # 1. nome, crm e especialidade não podem ser vazios (.strip())
        # 2. especialidade deve ser obrigatoriamente 'Cardiologia', 'Pediatria' ou 'Clinico Geral'
        #    Se vier qualquer outra, force para 'Clinico Geral' (sem derrubar o sistema)
        if not nome or not crm or not especialidade:
            raise ValueError(f'Nome, CRM e especialidade não podem ser vazios, tente novamente.')
        
        if especialidade.capitalize() not in ['Cardiologia', 'Pediatria', 'Clinico Geral']:
            especialidade = 'Clinico Geral'

        self._nome = nome
        self._crm = crm
        self._especialidade = especialidade
        self._agenda = [] # Lista de objetos da classe Consulta



    # ✍️ IMPLEMENTE:
    # 1. Getters (@property) para name, crm e especialidade

    @property
    def nome(self):
        return self._nome

    @property
    def crm(self):
        return self._crm
    
    @property
    def especialidade(self):
        return self._especialidade

    @property
    def agenda(self):
        return self._agenda

    # 2. Getter (@property) para agenda