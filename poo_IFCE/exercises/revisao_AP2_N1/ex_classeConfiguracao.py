'''
Crie a classe de configuração ConfiguracaoSistema que armazena em um dicionário privado __config as seguintes chaves fixas:
idioma, tema e volume.
Crie um método obter(chave) que retorna o valor de uma configuração e um método alterar(chave, valor) que atualiza o valor,
impedindo que uma chave inexistente seja adicionada e lançando um KeyError caso isso ocorra.
Instancie a classe, exiba as configurações, altere algumas e tente adicionar uma chave inválida.
'''

class ConfiguracaoSistema:

    __CONFIG = {'idioma':'pt-br', 'tema':'', 'volume':''}

    def obter(self, chave:str):
        return self.__CONFIG[chave]

    def alterar(self, chave:str, valor):
        if chave not in self.__CONFIG:
            raise KeyError(f'Chave não existe nas configurações.')
        self.__CONFIG[chave] = valor




configuracoes = ConfiguracaoSistema()
configuracoes.alterar('idioma', 'en-us')
print(f'{configuracoes.obter('idioma')}')