'''
# 31) Sistema auditoria:
# Crie classe Logger com __enter__ e __exit__.
# Registre início e fim de operação com WITH.
# Use print ou arquivo.
'''

class Logger:
    def __enter__(self):
        print(f'Inicio da operação. ')
        return self

    def __exit__(self, tipo_erro, valor_erro, traceback):
        if tipo_erro:
            print(f'ERRO DETECTADO: {valor_erro}')
        print(f'FIM DA OPERAÇÃO.')
        return False

with Logger() as log:
    print(f'EXECUTANDO OPERAÇÃO.')