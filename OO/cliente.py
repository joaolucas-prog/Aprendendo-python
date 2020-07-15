class Cliente:
    def __init__(self,nome):
        self.__nome = nome

    @property # seria um get diferenciado
    def nome(self):
        return self.__nome.title()
    @nome.setter
    def nome(self,nome):
        self.__nome = nome
