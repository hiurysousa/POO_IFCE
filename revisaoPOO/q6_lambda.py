'''
3. Conversor de Clima (Transformação de Dados)Você recebeu medições de temperatura de diferentes cidades em Celsius,
mas precisa delas em Fahrenheit:
(Cidade, Temperatura_C).Entrada: leituras = [("Manaus", 32), ("Curitiba", 15), ("Fortaleza", 29)]Objetivo:
Gerar uma lista de tuplas mantendo o nome da cidade, mas com a temperatura convertida.Fórmula: F = (temp x 1.8) + 32
'''

leituras = [("Manaus", 32), ("Curitiba", 15), ("Fortaleza", 29)]
temperaturas_f = list(map(lambda x: print(f'{x[0]}, {x[1] * 1.8 + 32}F°'), leituras))
