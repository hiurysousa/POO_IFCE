''' 5) Desenvolva classe Restaurante com nome endereco tipo e capacidade
 Implemente metodos reservar_mesa e exibir_cardapio do restaurante.'''
class Restaurante:

    def __init__(self, nome:str, endereco:str, tipo:str, capacidade:int):
        self.nome = nome
        self.endereco = endereco
        self.tipo = tipo
        self.capacidade = capacidade

    def reservar_mesa(self):
        print(f'Reservando mesa...')
        print(f'Info Geral: Restaurante {self.nome} | Endereço: {self.endereco}')


    def exibir_cardapio(self):
        print(f'Exibindo Menu...')


brasa = Restaurante('Brasa', 'Rua da Carne, 777', 'Churrascaria', 50)
brasa.reservar_mesa()
brasa.exibir_cardapio()