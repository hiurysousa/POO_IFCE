import rich
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibirEtiqueta(self):
        return f"{self.nome} || R$ {self.preco:.2f}"

    def __str__(self):
        return f"{self.nome} || R$ {self.preco:.2f}"

p1 = Produto("Memória Ram 16gb", 1000)
rich.inspect(p1)
print(p1)