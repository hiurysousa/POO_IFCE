'''# 21) Sistema cadastro:
# Leia idade do usuário.
# Lance ValueError se idade negativa.
# Exiba mensagem amigável ao usuário.
'''
try:
    age = int(input('Idade: '))
    if(age < 0):
        raise ValueError(f'Idade não pode ser negativa.')
    print(f'Cadastro realizado com sucesso.')
except ValueError as e:
    print(f'Erro de entrada: {e}')
    print(f'Please, write a positive number.')
