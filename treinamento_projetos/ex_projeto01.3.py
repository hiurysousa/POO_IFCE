'''
Cenário: Você está desenvolvendo o módulo de cadastro de conteúdos para uma plataforma de streaming de vídeo. O sistema precisa garantir que nenhum filme ou série seja publicado com dados corrompidos, durações impossíveis ou classificações fora do padrão legal.
class VideoConteudo {
        - id_codigo: String
        - titulo: String
        - duracao_minutos: int
        - classificacao: String
        + VideoConteudo(id_codigo, titulo, duracao_minutos, classificacao)
        + get_id_codigo() String
        + get_titulo() String
        + set_titulo(novo_titulo) void
        + get_duracao_minutos() int
        + set_duracao_minutos(nova_duracao) void
        + get_classificacao() String
    }
'''
class VideoConteudo:
    def __init__(self, id_codigo, titulo, duracao_minutos, classificacao):
        self.__id_codigo = id_codigo
        self.titulo = titulo
        self.duracao_minutos = duracao_minutos
        self.__classificacao = classificacao
    
    @property
    def id_codigo(self):
        return self.__id_codigo
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def duracao_minutos(self):
        return self.__duracao_minutos
    
    @property
    def classificacao(self):
        return self.__classificacao
    
    @titulo.setter
    def titulo(self, novo_titulo):
        self.__titulo = novo_titulo

    @duracao_minutos.setter
    def duracao_minutos(self, duracao):
        self.__duracao_minutos = duracao