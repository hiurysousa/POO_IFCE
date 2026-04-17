import rich

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        return f"Meu nome é {self.nome}, trabalho no setor de {self.setor} no cargo de {self.cargo}"

    def __str__(self):
        return f"Nome: {self.nome} | Setor: {self.setor} | Cargo: {self.cargo}"
f1 = Funcionario("Hiury", "Tecnologia", "Engenheiro de Dados")
rich.inspect(f1)
print(f1)
