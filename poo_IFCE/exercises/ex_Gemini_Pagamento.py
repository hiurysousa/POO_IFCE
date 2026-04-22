# 4) Sistema de Processamento de Pagamentos
# O objetivo é modelar um fluxo de checkout onde diferentes métodos de pagamento
# possuem regras de cálculo (taxas/descontos) e detalhes específicos.

#------------------------
# PAGAMENTO (Classe Base)
#------------------------
# # valor_bruto: float
#------------------------
# + Pagamento(valor_bruto: float)
# + calcular_valor_final(): float
# + detalhes(): str
#------------------------
class Pagamento:
    def __init__(self, valor_bruto):
        self._valor_bruto = valor_bruto

    def calcular_valor_final(self):
        return self._valor_bruto

    def detalhes(self):
        return f"Valor bruto: R$ {self._valor_bruto}"

#------------------------
# PAGAMENTO_CARTAO
#------------------------
# # taxa_fixa: float
# # parcelas: int
#------------------------
# + PagamentoCartao(valor_bruto: float, taxa_fixa: float, parcelas: int)
# + calcular_valor_final(): float
# + detalhes(): str
#------------------------
class Pagamento_Cartao(Pagamento):
    def __init__(self, valor_bruto, taxa_fixa, parcelas):
        super().__init__(valor_bruto)
        self._taxa_fixa = taxa_fixa
        self._parcelas = parcelas

    def calcular_valor_final(self):
        return super().calcular_valor_final() + self._taxa_fixa

    def detalhes(self):
        return f"Cartão ({self._parcelas}x) | " + super().detalhes()

#------------------------
# PAGAMENTO_BOLETO
#------------------------
#------------------------
# + PagamentoBoleto(valor_bruto: float)
# + calcular_valor_final(): float
# + detalhes(): str
#------------------------
class Pagamento_Boleto(Pagamento):
    def __init__(self, valor_bruto):
        super().__init__(valor_bruto)

    def calcular_valor_final(self):
        return super().calcular_valor_final() - (super().calcular_valor_final() * 0.1)

    def detalhes(self):
        return "Boleto (10% desc.) | " + super().detalhes()
#------------------------
# PAGAMENTO_PIX
#------------------------
# # chave_pix: str
#------------------------
# + PagamentoPix(valor_bruto: float, chave_pix: str)
# + calcular_valor_final(): float
# + detalhes(): str
#------------------------
class Pagamento_Pix(Pagamento):
    def __init__(self, valor_bruto, chave_pix):
        super().__init__(valor_bruto)
        self._chave_pix = chave_pix

    def calcular_valor_final(self):
        if self._valor_bruto <= 1000:
            return super().calcular_valor_final() - (super().calcular_valor_final() * 0.05)
        return super().calcular_valor_final() - (super().calcular_valor_final() * 0.1)

    def detalhes(self):
        return f"PIX (Chave: {self._chave_pix}) | " + super().detalhes()

def processar_fatura(pagamento):
    # Aqui o polimorfismo acontece: não importa a classe, chamamos os mesmos métodos
    valor_final = pagamento.calcular_valor_final()
    resumo = pagamento.detalhes()

    print(f"--- PROCESSANDO PAGAMENTO ---")
    print(f"Resumo: {resumo}")
    print(f"Total a pagar: R$ {valor_final:.2f}")
    print("-" * 30)
# Requisitos do Desafio:
# 1. Utilize Herança para conectar as subclasses à classe Pagamento.
# 2. Utilize super() para inicializar os atributos e reaproveitar comportamentos.
# 3. Regras de Cálculo (Polimorfismo):
#    - Cartão: valor_bruto + taxa_fixa.
#    - Boleto: 10% de desconto sobre o valor_bruto.
#    - Pix: 5% de desconto (ou 10% se o valor_bruto for > 1000).
# 4. Crie uma função externa processar_fatura(pagamento) que demonstre o polimorfismo
#    chamando os métodos calcular_valor_final() e detalhes() sem saber o tipo específico.

# --- Implemente seu código abaixo ---
# b) Instancie os objetos
cartao = Pagamento_Cartao(100, taxa_fixa=2.0, parcelas=3)
boleto = Pagamento_Boleto(100)
pix_pequeno = Pagamento_Pix(500, chave_pix="cpf-123")
pix_grande = Pagamento_Pix(1500, chave_pix="cnpj-456")

# c) Armazene em uma lista
lista_pagamentos = [cartao, boleto, pix_pequeno, pix_grande]

# d) Use o polimorfismo para processar todos
for p in lista_pagamentos:
    print("-" * 30)
    processar_fatura(p)