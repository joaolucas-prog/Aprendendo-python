# Criando uma Classe no python
class Conta:

    def __init__(self, numero, titular, saldo, limite):  # Criando um contrutor da classe
        print(
            "Criando uma conta {}".format(self))  # Self é uma referencia a classe crianda (Acho que é o mesmo que this)
        # criando atributos do objetos
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):#criando métodos no objeto
        print("O Saldo de {} é de : R${}".format(self.titular , self.saldo))

    def deposita(self,valor):
        self.saldo += valor
    def saca(self,valor):
        self.saldo -= valor
#para zerar o objeto utilizar o None que é equivalente ao null em Java
conta = Conta(123, "joao", 50, 500)
print(conta.numero)
conta.extrato()
conta.deposita(100)
conta.extrato()
conta.saca(50)
conta.extrato()

