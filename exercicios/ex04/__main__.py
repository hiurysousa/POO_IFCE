from aluno import Aluno
from professor import Professor
from funcionario import Funcionario
import rich


def main():
    aluno_um = Aluno('Hiury', 22, 'Ciência da Computação', 'S4')
    professor_um = Professor('Rodrigo', 47, 'Dados', 'Doutor')
    funcionario_um = Funcionario('Ronald', 24, 'Assistente', 'Coordenação')

    aluno_um.fazer_matricula()
    aluno_um.fazer_aniversario()
    rich.inspect(aluno_um)

    professor_um.estudar()
    funcionario_um.estudar()

if __name__ == "__main__":
    main()
