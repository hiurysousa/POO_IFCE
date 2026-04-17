'''
Você recebeu uma lista de e-mails de usuários, mas alguns estão com espaços em branco desnecessários e todos precisam estar em letras minúsculas para o banco de dados.

Entrada: emails_sujos = ["  USER1@gmail.com", "contato@Escola.br  ", "  Admin@site.Org "]

Objetivo: Use map e lambda para retornar uma lista onde cada e-mail esteja sem espaços nas bordas (strip()) e totalmente em minúsculo (lower()).

Dica: Você pode encadear os métodos dentro da lambda: lambda x: x.metodo1().metodo2().
'''

emails_sujos = ["  USER1@gmail.com", "contato@Escola.br  ", "  Admin@site.Org "]
emails_tratados = list(map(lambda email : email.strip().lower(), emails_sujos))
print(f'Emails sujos: {emails_sujos}')
print(f'Emails tratados: {emails_tratados}')