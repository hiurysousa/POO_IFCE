from medico import Medico
from paciente import Paciente
from consulta import Consulta

def main():
    print("=== TESTE 1: Criando Entidades ===")
    medico = Medico("Dr Drauzio", "12345", "Cardiologia")
    paciente = Paciente("Hiury Sousa", "123456789")
    
    print(f"Médico: {medico.nome} | Especialidade: {medico.especialidade}")
    print(f"Paciente: {paciente.nome} | CPF: {paciente.cpf}")

    print("\n=== TESTE 2: Agendando Consulta (Associação Automatizada) ===")
    # Criamos a consulta passando os objetos vivos
    consulta1 = Consulta("25/05/2026 14:00", medico, paciente)
    
    # Se a sua associação automática no construtor deu certo, 
    # o médico e o paciente já devem conhecer essa consulta!
    print(f"Consultas na Agenda do Médico: {len(medico.agenda)}")
    print(f"Consultas do Paciente: {len(paciente.consultas_agendadas)}")
    
    # Imprimindo o cruzamento de dados:
    print(f"\nDetalhe do prontuário: O paciente {paciente.consultas_agendadas[0].paciente.nome} "
          f"tem uma consulta com o {paciente.consultas_agendadas[0].medico.nome} "
          f"na data {paciente.consultas_agendadas[0].data_hora}")

if __name__ == "__main__":
    main()