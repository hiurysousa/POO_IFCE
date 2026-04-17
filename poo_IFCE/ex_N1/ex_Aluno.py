# 3) Implemente classe Aluno com nome matricula curso e notas.
# Crie metodo calcular_media e verificar_aprovacao do aluno.

class Aluno:

    def __init__(self, nome:str, matricula:str, curso:str):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.notas = []

    def calcular_media(self) -> float :
        if len(self.notas) != 0:
            media = sum(self.notas)/len(self.notas)
            return media
        else:
            return 0

    def verificar_aprovacao(self) -> bool:
        if self.calcular_media() >= 7.0:
            return True
        return False

    def adicionar_nota(self, nota:float) -> None:
        if nota >= 0 and nota <= 10:
            self.notas.append(nota)
        else:
            print('Nota inválida.')

aluno_um = Aluno('Hiury', '202610', 'Ciencia da Computacao')
aluno_um.adicionar_nota(7.5)
aluno_um.adicionar_nota(10)

print(f'Média {aluno_um.nome} = {aluno_um.calcular_media()} | Status Final: {'Aprovado' if aluno_um.verificar_aprovacao() else 'Reprovado'}')