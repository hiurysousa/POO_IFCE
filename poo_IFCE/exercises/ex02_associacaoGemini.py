'''
- nome: str
# integrantes: list[Desenvolvedor]
+ Equipe(nome: str)
+ integrantes: property (Getter que retorna a lista)
+ adicionar_integrante(dev: Desenvolvedor)
+ remover_integrante(dev: Desenvolvedor)
'''

class Equipe:
    def __init__(self, nome:str):
        self.nome = nome
        self._integrantes = []

    @property
    def integrantes(self):
        return self._integrantes

    def adicionar_integrante(self, desenvolvedor):
        if desenvolvedor not in self._integrantes:
            self._integrantes.append(desenvolvedor)
            desenvolvedor.definir_equipe(self)

    def remover_integrante(self, desenvolvedor):
        if desenvolvedor in self._integrantes:
            self._integrantes.remove(desenvolvedor)
            desenvolvedor.definir_equipe(None)

'''
+ nome: str
+ linguagem: str
# equipe: Equipe
+ Desenvolvedor(nome: str, linguagem: str)
+ equipe: property (Getter)
+ definir_equipe(equipe: Equipe)
'''
class Desenvolvedor:
    def __init__(self, nome:str, linguagem:str):
        self.nome = nome
        self.linguagem = linguagem
        self._equipe = None

    @property
    def equipe(self):
        return self._equipe

    def definir_equipe(self, equipe):
        if self._equipe != equipe:
            self._equipe = equipe
            if equipe is not None:
                equipe.adicionar_integrante(self)


equipe_um = Equipe('Squad Águia')
dev_um = Desenvolvedor('Alice', 'Python')
dev_dois = Desenvolvedor('Bob', 'Javascript')
equipe_um.adicionar_integrante(dev_um)
dev_dois.definir_equipe(equipe_um)

integrantes = [d.nome for d in equipe_um.integrantes]
print(integrantes)

print(f'{dev_um.nome} faz parte da equipe {dev_um.equipe.nome}')
