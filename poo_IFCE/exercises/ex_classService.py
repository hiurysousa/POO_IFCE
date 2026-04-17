class UserService:

    def cadastrar_usuario(self, nome, profissao, empresa, cidade):
        user = {
            "nome":nome,
            "profissao":profissao,
            "empresa":empresa,
            "cidade":cidade
        }
        print("Usuário cadastrado com sucesso.")
        return user

    def exibir_usuario(self, user):
        print(f"Nome: {user["nome"]}")
        print(f"Profissão: {user["profissao"]}")
        print(f"Empresa: {user["empresa"]}")
        print(f"Cidade: {user["cidade"]}")

    def atualizar_empresa(self, user, nova_empresa):
        user["empresa"] = nova_empresa



service = UserService()
u1 = service.cadastrar_usuario(
    'Hiury',
    'Engenheiro de Dados',
    'SPC',
    'Fortaleza'
)

service.exibir_usuario(u1)
service.atualizar_empresa(u1, 'DATAPREV')
print(f'\n')
service.exibir_usuario(u1)

