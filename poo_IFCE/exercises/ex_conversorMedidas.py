'''
# 9) Classe utilitária Conversor para operações matemáticas de unidades medida.
# Métodos estáticos: celsius_para_fahrenheit, metros_para_centimetros e quilos_para_gramas.
# Cada método deve receber um valor e retornar calculado.
# Use @staticmethod para definir cada uma das funções utilitárias.
# Teste as conversões chamando a classe sem criar um objeto.
'''

class Conversor:

    @staticmethod
    def celsius_fahrenheit(graus:float) -> float:
        return (graus*9/5) + 32

    @staticmethod
    def metros_centrimetros(metros:float) -> float:
        return metros*100

    @staticmethod
    def quilos_gramas(quilos:float) -> float:
        return quilos*1000

graus = 32
metros = 18
quilos = 50

print(f'32º são {Conversor.celsius_fahrenheit(graus)}F')
print(f'18 m são {Conversor.metros_centrimetros(metros)} cm')
print(f'50 kg são {Conversor.quilos_gramas(quilos)}g')