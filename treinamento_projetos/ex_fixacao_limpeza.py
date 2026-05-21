'''
Crie um laço for que percorra essa lista. Dentro do loop, utilize blocos try/except para tentar converter o "id"
para int e validar se o "nome" não está vazio (removendo os espaços com .strip()).
Se o dado for inválido (como o ID vazio ou o nome só com espaços), capture o erro e printe na tela:
"Pulando registro inválido". Ao final, exiba apenas a lista contendo os registros válidos convertidos.
'''

dados_brutos = [
    {"id": "1", "nome": "Hiury"},
    {"id": "", "nome": "Aluno Sem ID"},
    {"id": "3", "nome": "   "},
    {"id": "4", "nome": "Márcio"},
]
nova_lista = []
for i in dados_brutos:
    try:
        id_convertido = int(i["id"])
        nome = i["nome"].strip()
        if id_convertido > 0 and nome:
            registro_valido = {"id":id_convertido, "nome": nome}
            nova_lista.append(registro_valido)
        else:
            print(f'Pulando Registro Inválido')
    except ValueError:
        print(f'Pulando Registro Inválido.')


print(f'\n')
print(f'REGISTROS VÁLIDOS')
for itens in nova_lista:
    print(f'{itens}')
