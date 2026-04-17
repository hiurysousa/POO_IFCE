import rich
class Churrasco:
    # Atributos da classe
    consumo_padrao = 0.400 # cada pessoa come em média 400g de carne
    preco_kg = 82.40

    def __init__(self, pessoas):
        self.pessoas = pessoas

    def qtdCarne(self) -> float:
        return self.pessoas * Churrasco.consumo_padrao

    def custoTotal(self) -> float:
        return self.qtdCarne() * Churrasco.preco_kg

    def cpp(self) -> float: # custo por pessoa
        return self.custoTotal()/self.pessoas

    def __str__(self):
        return f"{self.pessoas} pessoas para o churrasco, totalizando {self.qtdCarne():.2f} KG de carne -> R${self.custoTotal():.2f} reais no total e R${self.cpp():.2f} por pessoa."
c1 = Churrasco(3)
rich.inspect(c1)
print(c1)