# Criando uma Classe no python
class Conta:
    def __init__(self,numero,titular,saldo,limite):#Criando um contrutor da classe
        print("Criando uma conta {}".format(self))#Self é uma referencia a classe crianda (Acho que é o mesmo que this)
        #criando atributos do objetos
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

conta = Conta(123,"joao",50,500)
print(conta.numero)
