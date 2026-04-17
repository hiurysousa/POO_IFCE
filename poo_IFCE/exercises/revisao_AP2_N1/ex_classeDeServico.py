'''
Uma biblioteca precisa de um sistema para gerenciar empréstimos de livros.
Crie a classe de serviço ServicoEmprestimo que possui uma lista privada __emprestimos para armazenar os empréstimos realizados.
Crie o método realizar_emprestimo(usuario, livro) que adiciona o empréstimo na lista como um dicionário com as
chaves usuario e livro. Crie o método listar_emprestimos() que exibe todos os empréstimos registrados e o
método total_emprestimos() que retorna a quantidade total. Instancie a classe, realize pelo menos 3 empréstimos e
exiba os resultados.
'''

class ServicoEmprestimo:

    def __init__(self):
        self.__emprestimos = []

    def realizar_emprestimo(self, usuario:str, livro:str):
        emprestimo = {'usuario':usuario, 'livro':livro}
        self.__emprestimos.append(emprestimo)

    def listar_emprestimos(self):
        for emprestimo in self.__emprestimos:
            print(f'{emprestimo}')

    def total_emprestimos(self):
        return len(self.__emprestimos)

servico = ServicoEmprestimo()
servico.realizar_emprestimo('Hiury', 'O Pequeno Príncipe')
servico.realizar_emprestimo('Rubens', 'O Poder do Hábito')
servico.realizar_emprestimo('Regina', 'Bíblia')
servico.listar_emprestimos()
print(f'Total de Empréstimos: {servico.total_emprestimos()}')