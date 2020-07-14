# Criando uma Classe no python
#Para deixar uma classe com acesso restrito equivalente ao privado em Java , utiliza "__" na frente do atributo
class Conta:

    def __init__(self, numero, titular, saldo, limite):  # Criando um contrutor da classe
        print(
            "Criando uma conta {}".format(self))  # Self é uma referencia a classe crianda (Acho que é o mesmo que this)
        # criando atributos do objetos
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):#criando métodos no objeto
        print("O Saldo de {} é de : R${}".format(self.__titular , self.__saldo))

    def deposita(self,valor):
        self.__saldo += valor
    def saca(self,valor):
        self.__saldo -= valor

    def transfere(self,valor, conta):
        self.saca(valor)
        conta.deposita(valor)
#para zerar o objeto utilizar o None que é equivalente ao null em Java
conta = Conta(123, "joao", 50, 500)
conta2 = Conta(321, "Ingrid", 100, 500)
print(conta._Conta__numero)# ele permite ainda acessar ,mas "Avisa que não é para fazer tal coisa"
print(conta._Conta__saldo)
#conta._Conta__saldo = 10000
#conta.extrato()
#conta.deposita(100)
#conta.extrato()
#conta.saca(50)
#conta.extrato()
conta.transfere(20,conta2)
conta.extrato()
conta2.extrato()

