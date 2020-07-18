#Existem alguns metodos magicos que fazem um certo comportamento por exemplo
#__init__ que gera um construtor
#__getitem__ que transforma em um interable
#__len__ que transforma em sizeble
#__str__ que é o "toString"
#PYTHON DATA MODEL
#iniciolização : __init__
#Representação __str__,__repr__
#Container , sequencia __contains__ , __iter__, __len__ , __getitem__
#Numericos __add__,__sub__,__mul__,__mod__
# para saber mais pesquisar sobre dunder metodos
#o bom que posso ditar oque alguns metodos podem fazer
#por exemplo se colocar o __add__ poderia dizer oque o simbolo + faz com o obj
#Ex: obj1 + obj2 isso adiciona obj2 no obj1 , ou coloca os elementos diferentes do obj1 no obj2 ...
#Criar um funcionalidade que vc deseja
# --------------------------------------------------------------------------------
#um pouco sobre classes abstratas , no python tem como fazer clsses abstratas porem n é muito recomendado
#pois ja pode existir uma classe base que ja possui aquelas caracteristicas e podemos herdar dela
# para isso usanmos o ABC abstract base classes
#ex: se eu quiser criar uma classe number e que ele vai herdar Number.Complex
#eu tenho que implementar os metodos exigidos daquela classe para que ela possa ser considerada um Complex
# e no python uma classe abstrata pode conter implementação ,diferente do java,e tb podemos usar essa
#implementação com o super()
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._like = 0

    def __str__(self):
        return f"Nome : {self._nome} - Ano: {self._ano} - Likes : {self._like}"

    def dar_like(self):
        self._like += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    @property
    def like(self):
        return self._like


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def retorna_cadastro_diferenciado(self):
        pass

    def __str__(self):
        return f"Nome : {self._nome} - Ano: {self._ano} - {self.duracao} min- Likes : {self._like}"


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"Nome : {self._nome} - Ano: {self._ano} - Temporadas :{self.temporadas}- Likes : {self._like}"

class Playlist():
    def __init__(self,nome,programas):
        self._programas = programas#
        self.nome = nome
    def __getitem__(self, item):# transformando a playlist em um obejeto interagil usando duck type (metodos magicos)
        return self._programas[item]
    def __len__(self):
        return len(self._programas)


vingadores = Filme("vingadores", 2018, 160)
dexter = Serie("Dexter", 2006, 6)
spn = Serie("SuperNatural",2006,12)
playlist = [vingadores, dexter,spn]
playlist1 = Playlist("playlist joao",playlist)


for programas in playlist1:#agora posso usar os metodos ja criados no objeto list na minha classe
    print(programas)

print(len(playlist1))
print(f"Está ? : {spn in playlist1 }")