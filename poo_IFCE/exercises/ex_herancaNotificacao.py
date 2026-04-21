# 3) Em um sistema de notificações, é necessário enviar mensagens por diferentes canais,
# como e-mail, SMS e push. Cada canal possui sua própria implementação,
# podendo inclusive ser desenvolvido por terceiros.
#
# Considere a seguinte especificação:
#
#------------------------
# EMAIL
#------------------------
# # endereco: str
#------------------------
# + Email(endereco: str)
# + enviar(mensagem: str)
#------------------------
#
#------------------------
# SMS
#------------------------
# # numero: str
#------------------------
# + SMS(numero: str)
# + enviar(mensagem: str)
#------------------------
#
#------------------------
# PUSH
#------------------------
# # dispositivo_id: str
#------------------------
# + Push(dispositivo_id: str)
# + enviar(mensagem: str)
#------------------------
#
# Implemente as classes acima em Python.
#
# Requisitos:
# 1. NÃO utilize herança entre as classes.
# 2. Todas as classes devem possuir o método enviar(mensagem).
# 3. Cada classe deve implementar o envio de forma distinta (ex: print identificando o canal).
#
# Ao final:
# a) Crie um trecho de código que:
# b) instancie um objeto de cada tipo (Email, SMS, Push);
# c) armazene-os em uma lista;
# d) percorra a lista e chame o método enviar("Olá!") para cada objeto.
#
# Observação:
# O objetivo é demonstrar Duck Typing — objetos diferentes, sem herança,
# sendo utilizados de forma uniforme com base no comportamento (método enviar).

class Email:
    def __init__(self, endereco):
        self._endereco = endereco

    def enviar(self, mensagem):
        print(f'Enviando: "{mensagem}" via email para {self._endereco}.')

class Sms:
    def __init__(self, numero):
        self._numero = numero

    def enviar(self, mensagem):
        print(f'Enviando: "{mensagem}" para o número {self._numero} via SMS.')

class Push:
    def __init__(self, dispositivo_id):
        self._dispositivo_id = dispositivo_id

    def enviar(self, mensagem):
        print(f'Enviando: "{mensagem}" para o dispositivo {self._dispositivo_id} via Push Notification.')

# --- Execução demonstrando Duck Typing ---

email_um = Email('teste@teste.com')
sms_um = Sms('99 8 6561-1405')
push_um = Push('2277')

# Aqui está o Duck Typing em ação: a lista contém tipos diferentes,
# mas todos possuem o comportamento 'enviar'.
canais_notificacao = [email_um, sms_um, push_um]

for canal in canais_notificacao:
    canal.enviar('Olá!')