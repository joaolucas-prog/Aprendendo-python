class Programa:
    def __init__(self,nome,ano):#Criando class Mae
        self._nome = nome.title()#um atributo privado da deep web
        self._ano = ano
        self._like = 0

    def __str__(self):#é o famoso toString do python
        return f"Nome : {self._nome} - Ano: {self._ano} - Likes : {self._like}"
    def dar_like(self):
        self._like +=1
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,nome):
        self._nome =  nome.title()

    @property
    def like(self):
        return self._like
class Filme(Programa):#Criando class filha
    def __init__(self,nome,ano,duracao):#chamando super
        super().__init__(nome,ano)
        self.duracao = duracao
    def retorna_cadastro_diferenciado(self):
        pass
    def __str__(self):
        return f"Nome : {self._nome} - Ano: {self._ano} - {self.duracao} min- Likes : {self._like}"

class Serie(Programa):
    def __init__(self,nome, ano , temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas
    def __str__(self):
        return f"Nome : {self._nome} - Ano: {self._ano} - Temporadas :{self.temporadas}- Likes : {self._like}"

vingadores = Filme("vingadores", 2018 , 160)
dexter = Serie("Dexter", 2006, 6)

playlist = [vingadores,dexter]

for programas in playlist:
    #detalhes = programas.duracao if hasattr(programas,'duracao') else programas.temporadas #if maneirão detalhes vai ser
    #igual ao programas.duracao se o atributo duracao tiver contido em programas

    #Removendo ifs e usando polimorfismo
    #programas.imprime()

    #Deixando mais pythonico
    print(programas)