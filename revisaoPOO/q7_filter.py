def par(number):
    return number % 2 == 0

minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_pares = list(filter(par, minha_lista))

print(lista_pares)