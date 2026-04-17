'''
Crie a classe utilitária ValidadorDados com métodos estáticos para validar informações de cadastro.
Implemente os métodos validar_cpf(cpf) que verifica se o CPF possui exatamente 11 dígitos numéricos,
validar_email(email) que verifica se o email contém @ e ., e validar_senha(senha) que verifica se a senha possui
no mínimo 8 caracteres. Cada método deve retornar True ou False. Nenhum método deve precisar de instância para ser chamado.
Teste cada validação diretamente pela classe com valores válidos e inválidos.
'''

class ValidadorDados:

    @staticmethod
    def validar_cpf(cpf:str):
        if len(cpf) == 11:
            return True
        return False

    @staticmethod
    def validar_email(email:str):
        if '@' in email:
            return True
        return False

    @staticmethod
    def validar_senha(senha:str):
        if len(senha) >= 8:
            return True
        return False

cpf = '00011122233'
email = 'teste@teste.com'
password = 'teste123'

print(f'{'CPF válido' if ValidadorDados.validar_cpf(cpf) else 'CPF inválido'}')
print(f'{'email válido' if ValidadorDados.validar_email(email) else 'email inválido'}')
print(f'{'senha válida' if ValidadorDados.validar_senha(password) else 'senha inválida'}')