# declaração de Classe
class Time:
    """
    Essa Classe permite a criação de objetos TIME
    Sendo assim, torna-se possível criar Time(nome, win, loses)
    """
    def __init__(self, name = "", win = 0, lose = 0): # Método construtor
        # Atributos de instância
        self.nome = name
        self.vitorias = win
        self.derrotas = lose
        self.tecnico = ""
        self.presidente = ""

    # Métodos de instância
    def vencer(self):
        self.vitorias += 1

    def perder(self):
        self.derrotas += 1

    def __str__(self):
        return f"{self.nome} tem {self.vitorias} vitórias e {self.derrotas} derrotas."

    def __getstate__(self):
        return f"Estado: Nome {self.nome} | Vitorias {self.vitorias} | Derrotas {self.derrotas}"
# declaração de Objeto
t1 = Time("Clube de Regatas Flamengo", 4, 1)
t1.vencer()
print(t1)

t2 = Time("Ceará Sport Club", 1, 3)

print(t2)
print(t2.__doc__) # ISSO EXIBE UMA ESPÉCIE DE MANUAL DA CLASSE

print(t1.__dict__) # atributo
print(t1.__getstate__()) # metodo