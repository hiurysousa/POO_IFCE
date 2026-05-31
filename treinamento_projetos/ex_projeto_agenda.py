'''
Agenda de Compromissos com Validação de Datas e Conflito de Horário
O Cenário: O professor quer testar sua capacidade de trabalhar com Strings que representam horários e manipulação de listas. Você criará um sistema de gerenciamento de reuniões que não permite dois compromissos no mesmo horário.

Regras de Negócio e Lógica:

A classe Compromisso recebe: titulo, data (string no formato "DD/MM/AAAA") e hora_inicio (string no formato "HH:MM", ex: "14:30"). Atributos protegidos.

A classe Agenda possui uma lista de compromissos.

Método agendar(compromisso): Antes de dar o .append(), o método deve varrer a agenda. Se já existir um compromisso na mesma data e na mesma hora de início, o sistema deve lançar uma Exceção Personalizada chamada ConflitoHorarioError.

Método listar_compromissos_da_data(data_pesquisa): Retorna uma lista com os compromissos daquela data, mas obrigatoriamente ordenados pelo horário de início (Dica: use .sort(key=...) extraindo os strings de hora).
'''

class ConflitoHorarioError(Exception):
    def __init__(self, data, hora_inicio):
        self.data = data
        self.hora_inicio = hora_inicio
        super().__init__(f'Já existe um compromisso para {data} - {hora_inicio}')



class Compromisso:
    def __init__(self, titulo, data, hora_inicio):
        self._titulo = titulo
        self._data = data
        self._hora_inicio = hora_inicio

    @property
    def titulo(self):
        return self._titulo
    
    @property
    def data(self):
        return self._data
    
    @property
    def hora_inicio(self):
        return self._hora_inicio

class Agenda:
    def __init__(self):
        self._compromissos = []

    def agendar(self, compromisso_novo):
        if not isinstance(compromisso_novo, Compromisso):
            raise TypeError(f'Objeto inválido.')

        for compromisso in self._compromissos:
            if compromisso.data == compromisso_novo.data and compromisso.hora_inicio == compromisso_novo.hora_inicio:
                raise ConflitoHorarioError(compromisso.data, compromisso.hora_inicio)
        
        self._compromissos.append(compromisso_novo)
       
            

    def listar_compromissos(self, data):
        for compromisso in self._compromissos:
            if compromisso.data == data:

                print(f'{compromisso.titulo} - {compromisso.data} - {compromisso.hora_inicio}')

compromisso_um = Compromisso('Projeto 03', '28/05/2026', '19:00')
compromisso_dois = Compromisso('Projeto 04', '28/05/2026', '20:30')
compromisso_tres = Compromisso('Final da Champions', '30/05/2026', '13:00')
compromisso_quatro = Compromisso('Corrida na beira do Rio', '30/05/2026', '13:00')


google_agenda = Agenda()

google_agenda.agendar(compromisso_dois)
google_agenda.agendar(compromisso_um)
google_agenda.agendar(compromisso_tres)
#google_agenda.agendar(compromisso_quatro)




google_agenda.listar_compromissos('28/05/2026')

