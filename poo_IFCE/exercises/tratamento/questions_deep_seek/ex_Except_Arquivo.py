'''
Uma escola está desenvolvendo um sistema para cadastrar alunos. O sistema deve validar a idade do aluno e, em caso de erro, registrar automaticamente a tentativa inválida em um arquivo de log.

Requisitos:
Crie uma classe de exceção personalizada chamada IdadeInvalidaError que herda de Exception.

A exceção deve receber o valor da idade informada e deve exibir uma mensagem informando que a idade é inválida e qual o intervalo permitido.

Crie um bloco try/except que:
Solicita ao usuário que digite a idade do aluno
Converte o valor para inteiro
Verifica se a idade está entre 6 e 18 anos (incluindo os extremos)
Se for inválida, lança a exceção IdadeInvalidaError passando o valor digitado
Se for válida, exibe a mensagem "Aluno cadastrado com sucesso! Idade: X anos"

No bloco except, utilize o gerenciador de contexto with para:
Abrir (ou criar) um arquivo chamado erros_idade.txt
Escrever a mensagem de erro completa no arquivo, incluindo a data e hora do erro
Garantir que o arquivo seja fechado automaticamente
O programa deve continuar executando normalmente após o erro, sem interromper.

Regras de validação:
A idade deve ser um número inteiro
A idade deve estar entre 6 e 18 anos (idade escolar)
Idades menores que 6 ou maiores que 18 devem ser rejeitadas

Exemplo de execução:
Caso o usuário digite 5:
Digite a idade do aluno: 5
Erro: Idade 5 anos é inválida. A idade permitida é entre 6 e 18 anos.
[Erro registrado no arquivo erros_idade.txt]

Caso o usuário digite 20:
Digite a idade do aluno: 20
Erro: Idade 20 anos é inválida. A idade permitida é entre 6 e 18 anos.
[Erro registrado no arquivo erros_idade.txt]

Caso o usuário digite 12:
Digite a idade do aluno: 12
Aluno cadastrado com sucesso! Idade: 12 anos

Conteúdo esperado do arquivo erros_idade.txt após uma execução com erro:
Idade 5 anos é inválida. A idade permitida é entre 6 e 18 anos.
'''

class IdadeInvalidaError(Exception):
    def __init__(self, idade):
        super().__init__(f'Idade inválida. Não foi possível cadastrar {idade} anos.')

try:
    age = int(input(f'Digite a idade do aluno: '))
    if age < 6 or age > 18:
        raise IdadeInvalidaError(age)
    else:
        print(f'Aluno cadastrado com sucesso! Idade: {age} anos')
except IdadeInvalidaError as e:
    with open('teste_prova.txt', 'w') as arquivo:
        arquivo.write(str(e))