# 2) Desenvolva classe Carro com marca modelo ano e quilometragem.
# Adicione metodos dirigir e calcular_consumo de combustivel.

class Carro:

    def __init__(self, marca:str, modelo:str, ano:int, quilometragem:float):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = quilometragem

    def dirigir(self, distancia:float):
        self.quilometragem += distancia
        print(f'Pé na estrada, distância percorrida {distancia} Km. Atualização: {self.quilometragem} km rodados.')


    def calcular_consumo(self, km_litro:float, distancia:float) -> float:
        return distancia/km_litro

    @property
    def exibir_info(self) -> None:
        print(f'Marca: {self.marca} | Modelo: {self.modelo} | Ano: {self.ano} | Quilometragem: {self.quilometragem}')

carro_um = Carro('Honda', 'Civic', 2018, 30000)
carro_um.exibir_info

distancia_viagem = 150
carro_um.dirigir(distancia_viagem)

consumo_estimado = carro_um.calcular_consumo(10, distancia_viagem)
print(f'Consumo estimado para {distancia_viagem} km: {consumo_estimado} L.')