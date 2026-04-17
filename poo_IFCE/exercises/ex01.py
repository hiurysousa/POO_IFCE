class User:

    def __init__(self, nome, profissao, empresa, cidade):
        self.nome = nome
        self.profissao = profissao
        self.empresa = empresa
        self.cidade = cidade

    def publicar(self, msg):
        print(f'{self.nome} publicou em seu perfil: ')
        print(msg)

    def exibir_perfil(self):
        print('=== PERFIL ===')
        print(f'Nome: {self.nome}')
        print(f'Profissão: {self.profissao}')
        print(f'Empresa: {self.empresa}')
        print(f'Cidade: {self.cidade}')


user_1 = User('Hiury', 'Data Engineer', 'SPC', 'Aracati')
user_2 = User('Witalo', 'Cyber Security', 'CISCO', 'Icapui')

user_1.exibir_perfil()
print('\n')
user_1.publicar('Parabéns pela contratação, você merece.')
print('\n')
user_2.exibir_perfil()