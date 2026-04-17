'''
# 8) Classe de serviço NotificacaoService para gerenciar envio de mensagens.
# Atributo: historico (lista).
# Método enviar_email recebe destinatario e mensagem.
# O método deve adicionar o email ao histórico de envios.
# Método listar_enviados: percorre e exibe todos os emails da lista.
# Instancie o serviço e simule o envio de três emails.
'''

class NotificacaoService:

    def __init__(self):
        self.historico = []

    def enviar_email(self, destinatario:str, email:str):
        mensagem = {destinatario, email}
        self.historico.append(mensagem)

    def listar_enviados(self):
        for mensagem in self.historico:
            print(f'{mensagem}')


servico = NotificacaoService()
servico.enviar_email('jp-fernandes@gmail.com', 'ola, seja bem vindo!')
servico.enviar_email('matue@gmail.com', 'pvt é sal!')
servico.enviar_email('tz@gmail.com', 'aguia so anda com aguia')

servico.listar_enviados()