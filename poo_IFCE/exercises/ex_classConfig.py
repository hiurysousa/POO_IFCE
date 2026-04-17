'''
SistemaConfig
'''

class SistemaConfig:

    MAX_TENTATIVAS_LOGIN = 3
    TAMANHO_MAX_UPLOAD_MB = 50
    MODO_DEBUG = True
    TEMPO_EXPIRACAO_SESSAO = 15

print('##### Sistema Configurado com Base na Classe SistemaConfig #####')
print(f'\nMáximo de tentativas de login {SistemaConfig.MAX_TENTATIVAS_LOGIN}')
print(f'Tamanho máximo para upload {SistemaConfig.TAMANHO_MAX_UPLOAD_MB}')

print('Sistema em MODO DEBUG.') if SistemaConfig.MODO_DEBUG else print('Modo debug desativado.')
print(f'Tempo máximo de sessão: {SistemaConfig.TEMPO_EXPIRACAO_SESSAO} minutos.')
