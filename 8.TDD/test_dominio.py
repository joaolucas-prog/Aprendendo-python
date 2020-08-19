from unittest import TestCase #importando a classe de teste do python
from dominio import Usuario , Lance , Leilao , Avaliador

class TestAvaliador(TestCase):
    def test_avalia(self):
        gui = Usuario('Gui')
        yuri = Usuario("Yuri")

        lance_yuri = Lance(yuri, 140.0)
        lance_gui = Lance(gui, 100.0)

        leilao = Leilao("Celular")

        leilao.lances.append(lance_gui)
        leilao.lances.append(lance_yuri)

        avaliador = Avaliador()
        avaliador.avalia(leilao)
        menor_valor_esperado = 100.0
        maior_valor_esperado = 140.0

        self.assertEqual(menor_valor_esperado,avaliador.menor_lance) #verifica a igualdade
        self.assertEqual(maior_valor_esperado,avaliador.maior_lance) #verifica a igualdade
