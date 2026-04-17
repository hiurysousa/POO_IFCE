'''
1. Folha de Pagamento (Soma de Valores)
Você tem uma lista de funcionários onde cada tupla contém: (Nome, Salário Base, Valor da Hora Extra, Quantidade de Horas Extras).

Entrada: funcionarios = [("Ana", 3000, 50, 10), ("Carlos", 2500, 40, 5), ("Bia", 4000, 60, 2)]

Objetivo: Gerar uma lista com o salário total de cada um (Salário Base + (Valor Hora * Qtd Hora)).
'''

funcionarios = [("Ana", 3000, 50, 10), ("Carlos", 2500, 40, 5), ("Bia", 4000, 60, 2)]

lista_pagamento = list(map(lambda x: x[1] + (x[2] * x [3]), funcionarios))

print(lista_pagamento)
