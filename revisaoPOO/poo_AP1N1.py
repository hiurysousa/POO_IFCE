""""
Uma empresa deseja classificar seus clientes com base na pontuação de compras e na frequência de visitas. Escreva um programa em Python que solicite a pontuação acumulada (número inteiro positivo) e solicite a quantidade de visitas no mês (número inteiro positivo). Com base nesses dados, classifique o cliente como:
"Cliente Premium": se a pontuação for maior que 500 e tiver mais de 10 visitas;
"Cliente Fiel": se a pontuação for entre 300 e 500 (inclusive) e tiver ao menos 5 visitas;
"Cliente Iniciante": se a pontuação for abaixo de 300, mas com pelo menos 1 visita;
"Cliente Inativo": se tiver 0 visitas, independentemente da pontuação.
"""

while True:
    pontuacao = int(input('Digite a pontuação do usuário (-1 p/ sair): '))
    if pontuacao == -1:
        break
    visita = int(input('Digite a quantidade de visitas do usuário: '))
    if pontuacao > 500 and visita > 10:
        print(f'Cliente Premium !')
    elif  500 >= pontuacao > 300 and visita <= 5:
        print(f'Cliente Fiel !')
    elif pontuacao < 300 and visita > 0:
        print(f'Cliente Iniciante !')
    elif visita == 0:
        print(f'Cliente Inativo !')

