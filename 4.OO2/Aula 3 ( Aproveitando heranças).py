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


#class Playist(list): # Posso herdar as caracteristicas do objeto list na minha classe ( SHOW!!)
                      # Porem isso tudo iria criar um complexidade muito grande no meu código pois,teria que saber
                      #toda a documentação da class list para não sobrescrever algo que não poder
                     #ou outras coisas
class Playlist():
    def __init__(self,nome,programas):
        self._programas = programas#Porem o codigo assim ainda n está legal , por isso usaremos as funcionalidades do
        #python para melhora-lo
        self.nome = nome
    def __getitem__(self, item):# transformando a playlist em um obejeto interagil usando duck type
        return self._programas[item]
    #@property
    #def tamanho(self):
    #    return len(self._programas)
    #@property
    #def listagem(self):
    #    return self._programas

vingadores = Filme("vingadores", 2018, 160)
dexter = Serie("Dexter", 2006, 6)
spn = Serie("SuperNatural",2006,12)
playlist = [vingadores, dexter,spn]
playlist1 = Playlist("playlist joao",playlist)


for programas in playlist1:#agora posso usar os metodos ja criados no objeto list na minha classe
    print(programas)

print(len(playlist1))
print(f"Está ? : {spn in playlist1 }")