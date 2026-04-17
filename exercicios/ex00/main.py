# declaração de Classe
class Time:
    def __init__(self): # Método construtor
        # Atributos de instância
        self.nome = ""
        self.vitorias = 0
        self.empates = 0
        self.tecnico = ""
        self.presidente = ""

    # Métodos de instância
    def vencer(self):
        self.vitorias += 1

    def empate(self):
        self.empates += 1

    def mensagem(self):
        return f"{self.nome} tem {self.vitorias} vitórias e {self.empates} empates."

# declaração de Objeto
t1 = Time()
t1.nome = "Clube de Regatas Flamengo"
t1.vitorias = 4
t1.vencer()
print(t1.mensagem())

t2 = Time()
t2.nome = "Ceará"
t2.vitorias = 1
print(t2.mensagem())