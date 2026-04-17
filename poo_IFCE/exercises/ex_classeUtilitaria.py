class TextoUtil:

    @staticmethod
    def contar_caracteres(texto:str) -> int:
        texto_novo = texto.replace(' ', '')
        return len(texto_novo)

    @staticmethod
    def contar_palavras(texto:str) -> int:
        return len(texto.split())

    @staticmethod
    def texto_maiusculo(texto:str) -> str:
        return texto.upper()

    @staticmethod
    def texto_minusculo(texto:str) -> str:
        return texto.lower()

frase = 'Essa é minha atividade para a disciplina de POO.'
print(f'Quantidade de caracteres: {TextoUtil.contar_caracteres(frase)}')
print(f'Quantidade de palavras: {TextoUtil.contar_palavras(frase)}')
print(f'Frase em maiúscula: {TextoUtil.texto_maiusculo(frase)}')
print(f'Frase em minúscula: {TextoUtil.texto_minusculo(frase)}')

