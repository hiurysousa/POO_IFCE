'''
# 10) Classe abstrata chamada Animal usando o módulo abc do Python.
# Atributos: nome e idade. Método abstrato chamado emitir_som().
# Método comum chamado dormir que exibe uma mensagem padrão.
# Tente instanciar a classe Animal e explique o erro ocorrido. Resposta = Can't instantiate abstract class Animal without an implementation for abstract method 'emitir_som'
# Crie uma subclasse Cachorro que implementa o método emitir_som.
'''
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        print('Au')

class Gato(Animal):
    def emitir_som(self):
        print('Miau')

dog = Cachorro()
dog.emitir_som()

cat = Gato()
cat.emitir_som()