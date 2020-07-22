class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Criando uma conta {}".format(self))
        ATRIBUTOESTATICO = "Atributo estatico XD" #Criando um atributo estatico
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigoBanco = "001"
    def extrato(self):
        print("O Saldo de {} é de : R${}".format(self.__titular , self.__saldo))

    def deposita(self,valor):
        self.__saldo += valor

    def __podeSacar(self,valor):#Criando método privado
        valorDisponivelSacar = self.__saldo + self.__limite
        return (valor <= valorDisponivelSacar)

    def saca(self,valor):
        if(self.__podeSacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self,valor, conta):
        self.saca(valor)
        conta.deposita(valor)
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self,valor):
        self.__saldo = valor
    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self,limite):
        self.__limite = limite
    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self,titular):
        self.__titular = titular
    @staticmethod #criando um metodo estatico
    def codigoBanco():
        return "001"

