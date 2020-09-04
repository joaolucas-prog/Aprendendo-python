class Usuario:

    def __init__(self,nome, carteira):
        self.__nome = nome
        self.__carteira = carteira
    def propoe_lance(self, leilao , valor):
        if self._valor_eh_valido(valor):
            lance = Lance(self,valor)
            leilao.propoe(lance)
            self.__carteira -= valor
        else:
            raise ValueError("valor maior que sua carteira!!")

    @property
    def nome(self):
        return self.__nome
    @property
    def carteira(self):
        return self.__carteira

    def _valor_eh_valido(self,valor):
        return valor <= self.__carteira


class Lance:

    def __init__(self,usuario , valor):
        self.usuario = usuario
        self.valor = valor

class Leilao:
    def __init__(self,descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    def propoe(self, lance : Lance):
        if self._lance_eh_valido(lance) :
            if not self._tem_lance():
                self.menor_lance = lance.valor

            self.maior_lance = lance.valor

            self.__lances.append(lance)
        else:
            raise ValueError("Error ao tentar fazer um lance")
    def _tem_lance(self):
        return self.__lances

    def _usuarios_diferente(self,lance):
        return self.__lances[-1].usuario != lance.usuario

    def _lance_eh_maior(self,lance):
        return lance.valor > self.lances[-1].valor

    def _lance_eh_valido(self,lance):
        return not self._tem_lance() or (self._usuarios_diferente(lance) and self._lance_eh_maior(lance))

    @property
    def lances(self):
        return self.__lances

