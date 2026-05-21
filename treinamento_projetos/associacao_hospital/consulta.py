from medico import Medico
from paciente import Paciente

class Consulta:
    def __init__(self, data_hora: str, medico_obj: Medico, paciente_obj: Paciente):
        # ✍️ SUA LÓGICA DE VALIDAÇÃO:
        # 1. data_hora não pode ser vazia
        # 2. Valide se medico_obj é uma instância real de Medico (isinstance)
        # 3. Valide se paciente_obj é uma instância real de Paciente (isinstance)
        # *Se falhar:* lance ValueError
        if not data_hora:
            raise ValueError(f'Erro, data_hora não pode ser vazia.')
        
        if not isinstance(medico_obj, Medico) or not isinstance(paciente_obj, Paciente):
            raise ValueError(f'Objeto médico e paciente devem ser válidos.')
        

        
        self._data_hora = data_hora
        self._medico = medico_obj
        self._paciente = paciente_obj
        medico_obj.agenda.append(self)
        paciente_obj.consultas_agendadas.append(self)


        # ---------------------------------------------------------------------
        # ✍️ SEU DESAFIO DE ASSOCIAÇÃO BIDIRECIONAL:
        # Assim que a consulta nascer com sucesso, ela deve se auto-adicionar:
        # 1. Na lista '_agenda' do objeto médico recebido
        # 2. Na lista '_consultas_agendadas' do objeto paciente recebido
        # ---------------------------------------------------------------------
        # Dica: dentro do construtor, você pode acessar métodos dos objetos recebidos
        # ex: medico_obj.agenda.append(self)
        
    # ✍️ IMPLEMENTE:
    # Getters para data_hora, medico e paciente

    @property
    def data_hora(self):
        return self._data_hora
    
    @property
    def medico(self):
        return self._medico
    
    @property
    def paciente(self):
        return self._paciente