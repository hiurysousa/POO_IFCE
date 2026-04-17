'''
# 7) Classe de configuração chamada AppConfig para armazenar dados globais.
# Atributos de classe: nome_app, versao, idioma_padrao e ambiente_execucao.
# Não instancie esta classe, use apenas os atributos diretamente.
# Exiba o nome do aplicativo e a versão no console.
# Verifique se o idioma padrão está definido como português.
'''

class AppConfig:

    NOME_APP = 'TikTok'
    VERSAO = '2.16'
    IDIOMA_PADRAO = 'PT-BR'


print(f'Nome do aplicativo {AppConfig.NOME_APP} | Versão: {AppConfig.VERSAO}')
print(f'{'Aplicativo em PT-BR' if AppConfig.IDIOMA_PADRAO == 'PT-BR' else 'Aplicativo em outro idioma'}')