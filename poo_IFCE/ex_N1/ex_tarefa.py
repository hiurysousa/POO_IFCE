# 4) Crie classe Tarefa com descricao data prazo e status.
# Adicione metodos marcar_concluida e exibir_detalhes da tarefa.

class Tarefa:

    def __init__(self, descricao:str, data_prazo:str, status:str):
        self.descricao = descricao
        self.data_prazo = data_prazo
        self.status = status

    def marcar_concluida(self) -> None:
        self.status = 'Concluída'


    def exibir_detalhes(self):
        print(f'## Tarefa para o dia {self.data_prazo} ##')
        print(f'-- Descrição: {self.descricao}')
        print(f'Status: {self.status}')

tarefa_faculdade = Tarefa('Fazer trabalho de Cálculo Numérico', '08/04/2026', 'Andamento')
tarefa_faculdade.marcar_concluida()
tarefa_faculdade.exibir_detalhes()

