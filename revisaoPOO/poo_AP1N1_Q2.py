"""
Considere uma tupla de valores que pode conter números e strings como em (3, 9, '7', 12, 'onze', 18, 21). O programa deve:
a) Solicitar ao usuário um número entre 1 e 100, permitindo que o programa prossiga apenas caso a entrada seja válida.
b) Exiba todos os números ímpares da tupla que são maiores que o valor inserido.
c) Exiba a quantidade total de valores válidos (int ou float) que foram considerados no filtro.

Referência: a função built-in isinstance(variável, tipo) em Python verifica se determinada "variável" é do "tipo" especificado, retornando True ou False.
"""

minha_tupla = (3, 9, '7', 12, 'onze', 18, 21.0)
tupla_maiores = ()
contador = 0
while True:
    user = int(input('Digite um numero de 1 - 100: '))
    if 0 < user <= 100:
        for valor in minha_tupla:
            if isinstance(valor, int) == True or isinstance(valor, float) == True:
                contador += 1
                if valor > user and valor % 2 != 0:
                    tupla_maiores += (valor,)
        break
    else:
        print(f'Valor inválido.')

print(f'Valores maiores que o numero digitado pelo usuário: {tupla_maiores} ')
print(f'Quantidade de valores válidos na tupla {contador}')
