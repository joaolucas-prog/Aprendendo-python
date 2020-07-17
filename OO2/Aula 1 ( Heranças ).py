# para definir uma herança no python vc cria uma classe normal e depois quando for criar uma classe filha
# vc usa o class classe_filho(classe_mae):
# e chamar o metodo super(atributos da classe mae)
#em pythom por enquanto não sei uma forma de deixar os metodos da classe mae privada pq da erro
#então coloca apenas 1 _ para simular o privado e vida que segue
class Programa:
    def __init__(self,nome,ano):#Criando class Mae
        self._nome = nome.title()#um atributo privado da deep web
        self._ano = ano
        self._like = 0
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

class Serie(Programa):
    def __init__(self,nome, ano , temporadas):
        super().__init__(nome,ano)
        self.__temporadas = temporadas

vingadores = Filme("vingadores", 2018 , 160)
dexter = Serie("Dexter", 2006, 6)

print(f"{vingadores.nome} - {vingadores._ano} - {vingadores.duracao}")