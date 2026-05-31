from membro_estudante import MembroEstudante
from unidade_academia import UnidadeAcademia
from membro_vip import MembroVip

# Insira os seus imports aqui conforme a estrutura das suas pastas

# 1. Criando a filial
academia = UnidadeAcademia("GymControl - IFCE")

# 2. Criando os membros (Repare nos argumentos que acionam o super())
aluno_estudante = MembroEstudante("Hiury Sousa", "12345", 100.0, "IFCE")
aluno_vip = MembroVip("Valter Professor", "54321", 100.0, 60.0)

# 3. Efetuando as matrículas
academia.matricular_membro(aluno_estudante)
academia.matricular_membro(aluno_vip)

# 4. Registrando treinos (Método herdado da classe mãe)
aluno_estudante.registrar_treino("Costas e Bíceps")
aluno_vip.registrar_treino("Perna Completo")

# 5. Validações de Saída
print(f"Mensalidade Hiury (Estudante com 20% desc): R$ {aluno_estudante.calcular_mensalidade()}") 
# Deve exibir: 80.0

print(f"Mensalidade Valter (VIP com taxa extra): R$ {aluno_vip.calcular_mensalidade()}") 
# Deve exibir: 160.0

print(f"Faturamento Total da Academia: R$ {academia.faturamento_total()}") 
# Deve exibir: 240.0

print(f"Histórico de treinos do Hiury: {aluno_estudante.historico_treinos}")