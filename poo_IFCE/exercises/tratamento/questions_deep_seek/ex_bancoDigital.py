'''
Contexto: Sistema bancário onde duas contas podem transferir dinheiro entre si.

Regras:
Não pode transferir valor negativo ou zero
Saldo da conta origem deve ser suficiente

Sua tarefa:
Crie a classe ValorInvalidoError que herda de Exception
Ela deve receber o valor informado no construtor
A mensagem deve ser: "Valor R${valor} inválido. Use um valor positivo."
Crie a classe SaldoInsuficienteError que herda de Exception
Ela deve receber no construtor: saldo_atual e tentativa_transferencia


Crie a classe ContaDigital com os seguintes atributos: titular, numero_conta, saldo
Crie o método transferir que recebe dois parâmetros: destino e valor
Dentro do método transferir:
Se valor for menor ou igual a zero, lance ValorInvalidoError
Se valor for maior que o saldo, lance SaldoInsuficienteError
Se tudo estiver correto, debite o valor da conta origem e credite o valor na conta destino
'''
class ValorInvalidoError(Exception):
    def __init__(self, valor):
        self.valor = valor
        super().__init__(f'Valor R${valor} inválido. Use um valor positivo.')

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo_atual, tentativa_transferencia):
        self.saldo_atual = saldo_atual
        self.tentativa_transferencia = tentativa_transferencia
        super().__init__(f'Não foi possível transferir R$ {tentativa_transferencia}, saldo atual -> R$ {saldo_atual}')

class ContaDigital:
    def __init__(self, titular, numero_conta, saldo):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo

    def transferir(self, destino, valor):
        if valor < 0:
            raise ValorInvalidoError(valor)
        elif valor > self.saldo:
            raise SaldoInsuficienteError(self.saldo, valor)
        print(f'R$ {valor} transferido para {destino.titular}')
        self.saldo -= valor
        destino.saldo += valor
        print(f'Saldo atual atualizado: R$ {self.saldo}')

minha_conta = ContaDigital('Hiury Sousa', 1010, 500)
conta_clara = ContaDigital('Clara', 2020, 50)

minha_conta.transferir(conta_clara, 50)
print(f'Saldo Clara: {conta_clara.saldo}')

