'''
3. Nível Médio: Filtro de Tipos com Zip
Você tem duas listas: uma com nomes de sensores e outra com as leituras (algumas leituras vieram como None por erro).
sensores = ["Temp", "Umidade", "Pressao"]
leituras = [25.5, None, 1012]

Objetivo: Utilize zip para iterar sobre as duas ao mesmo tempo. Dentro do loop, use isinstance ou type para exibir apenas os sensores que possuem leitura numérica válida (float ou int).
'''

sensores = ["Temp", "Umidade", "Pressao"]
leituras = [25.5, None, 1012]


lista_filtro = list(zip(sensores, leituras))
for sensor, leitura in lista_filtro:
    if isinstance(leitura, (int, float)):
        print(f'Sensor: {sensor} || Leitura: {leitura}')

