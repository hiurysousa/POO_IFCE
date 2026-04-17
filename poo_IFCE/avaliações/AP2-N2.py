'''
Desenvolva uma classe utilitária para servir de Agenda Telefônica. Implemente métodos para
adicionar, remover e buscar contatos na agenda. É importante que os dados da agenda fiquem protegidos contra
vazamento de dados, então utilize encapsulamento.
'''

class AgendaTelefonica:
    __lista = []

    @classmethod
    def adicionar(cls, telefone:str) -> None:
        cls.__lista.append(telefone)

    @classmethod
    def remover(cls, telefone:str) -> None:
        if telefone in cls.__lista:
            cls.__lista.remove(telefone)
        else:
            print(f'{telefone} não encontrado na agenda.')

    @classmethod
    def buscar(cls, telefone:str) -> bool:
        if telefone in cls.__lista:
            return True
        return False

    @classmethod
    def exibir(cls) -> str:
        for valor in cls.__lista:
            print(f'{valor}')

AgendaTelefonica.adicionar('88 9 7777-3333')
AgendaTelefonica.adicionar('85 9 4444-3333')
AgendaTelefonica.adicionar('21 9 8888-5555')

AgendaTelefonica.remover('88 9 7777-3333')
AgendaTelefonica.exibir()
print(f'{'Número encontrado.' if AgendaTelefonica.buscar('21 9 8888-5555') else 'Número não encontrado.'}')
