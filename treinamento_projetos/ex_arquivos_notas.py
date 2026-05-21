'''
Escreva um script em Python que abra esse arquivo usando with, leia todas as notas,
converta-as de string para número decimal (float), calcule a média aritmética
dessas notas e exiba o resultado no terminal.
'''

with open("data/notas.txt", "r") as arquivo:
    notas = []
    for linha in arquivo:
        notas.append(float(linha))
    print(f'Media: {sum(notas)/len(notas)}')