'''
Em um sistema de saúde, é necessário modelar a entidade Medico e a entidade Paciente.
Como um médico presta serviço ao paciente, mas ambos existem de forma independente, temos uma relação de ASSOCIAÇÃO.
- nome: str
- crm: str
# pacientes: list[Paciente]

+ Medico(nome: str, crm: str)
+ pacientes: property
+ adicionar_paciente(paciente: Paciente)
+ remover_paciente(paciente: Paciente)
'''
class Medico:
    def __init__(self, nome:str, crm:str):
        self.nome = nome
        self.__crm = crm
        self._pacientes = []

    @property
    def pacientes(self):
        return self._pacientes

    def adicionar_paciente(self, paciente):
        if paciente not in self._pacientes:
            self._pacientes.append(paciente)
            if paciente.medico_responsavel != self:
                paciente.definir_medico(self)
        else:
            raise TypeError('Não foi possível adicionar o paciente na lista.')

    def remover_paciente(self, paciente):
        if paciente in self._pacientes:
            self._pacientes.remove(paciente)
            if paciente.medico_responsavel == self:
                paciente.definir_medico(None)
        else:
            raise TypeError('Paciente não encontrado')

'''
+ nome: str
+ cpf: str
# medico_responsavel: Medico

+ Paciente(nome: str, cpf: str)
+ medico_responsavel: property
+ definir_medico(medico: Medico)
'''

class Paciente:
    def __init__(self, nome:str, cpf:str):
        self.nome = nome
        self.cpf = cpf
        self._medico_responsavel = None

    @property
    def medico_responsavel(self):
        return self._medico_responsavel

    def definir_medico(self, medico):
        if self._medico_responsavel != medico:
            self._medico_responsavel = medico
            if medico is not None:
                if self not in medico.pacientes:
                    medico.adicionar_paciente(self)

medico_um = Medico('Dr Drauzio', '222333')
paciente_um = Paciente('Marcos', '444555666')
paciente_dois = Paciente('Pamela', '999888777')

medico_um.adicionar_paciente(paciente_um)
paciente_dois.definir_medico(medico_um)

for pacientes in medico_um.pacientes:
    print(f'Paciente: {pacientes.nome}')

''' ou
nomes = [p.nome for p in medico_um.pacientes]
print(nomes)
'''

print(f'Paciente {paciente_um.nome}: {paciente_um.medico_responsavel.nome}')
print(f'Paciente {paciente_dois.nome}: {paciente_dois.medico_responsavel.nome}')


