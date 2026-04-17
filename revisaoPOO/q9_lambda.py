'''
5. Validação de Cadastro (Lógica Condicional)
Você tem uma lista de usuários com: (Username, Idade).

Entrada: usuarios = [("admin_99", 25), ("user_teen", 15), ("tester_01", 18)]

Objetivo: Usar map e lambda para retornar uma lista de strings: "Autorizado" se
a idade for maior ou igual a 18, e "Negado" caso contrário.
'''

usuarios = [("admin_99", 25), ("user_teen", 15), ("tester_01", 18)]
autorizacao = list(map(lambda x : 'Autorizado' if x[1] >= 18 else 'Negado', usuarios))
print(autorizacao)
