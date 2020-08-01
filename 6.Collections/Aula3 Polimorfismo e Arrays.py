# UTILIZANDO POLIMORFISMO COM LISTA
class Conta:
    def __init__(self,codigo):
        self._codigo = codigo
        self._saldo = 0
    def deposita(self,valor):
        self._saldo += valor
    def __str__(self):
        return f"[>>Código {self._codigo} Saldo {self._saldo}<<]"

class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

conta_joao = ContaCorrente(1341)
conta_joao.deposita(1000)
conta_ingrid = ContaPoupanca(1000)
conta_ingrid.deposita(1000)

contas = [conta_joao,conta_ingrid]

for conta in contas:
    conta.passa_o_mes() #Duck type
print(conta_joao)
print(conta_ingrid)

"""
Array em python deve ser evitado , ele é utilizado para melhor perfomarce de tipos numericos, para isso 
é melhor utilizar a biblioteca numpy
"""
import array as arr
a = arr.array('d',[1,3.5]) #Criando um Array de numeros flutoantes
print(a)
import numpy as np
numeros = np.array([1,3.5])#utilizando a biblioteca numpy
print(numeros)
"""
Metodos abstratos , Caso eu queira criar uma classe Mãe e que eu obrigue todas as futuras classes
filhas a ter um método especifico eu posso definir um metodo abstrato para isso preciso
definir minha metaclasse da classe como ABCMeta e utilizar o @abstractmethods
"""
from abc import ABCMeta,abstractmethod
class Conta2(metaclass=ABCMeta):
    def __init__(self,codigo):
        self._codigo = codigo
        self._saldo = 0
    def deposita(self,valor):
        self._saldo += valor
    @abstractmethod
    def passa_o_mes(self):
        pass
    def __str__(self):
        return f"[>>Código {self._codigo} Saldo {self._saldo}<<]"

"""
IGUALDADE EM UMA CLASSE

para defenir uma igualdade de uma classe criada eu devo ter um metodo especial __eq__(self,outro):
e definir quais condições fazem com que elas sejam iguais

posso dizer que um atributo igual a outra torna as 2 variaveis iguais, ou o tipo de classe são iguais
ou isinstance da classe ou seja se é a propria classe ou classe filha
"""