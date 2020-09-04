from unittest import TestCase #importando a classe de teste do python
from dominio import Usuario , Lance , Leilao

class TestLeilao(TestCase):

    #Caso você copie e cole cenarios em 2 ou mais métodos é bom voce criar um cenario isolado
    #onde aquela parte será igual a ambas, para quando modificar em um local servir para todos os outros
    def setUp(self):#com o metodo setUp(self) ele será invocado em todos os outros metodos sem precisar
                    #inicializa-lo e ele sempre é "zerado" quando chamado em outro metodo

        #OBS coloque apenas objetos que são comuns em TODAS os metodos por questão de performace 
        self.gui = Usuario('Gui',200)
        self.lance_gui = Lance(self.gui, 100.0)
        self.leilao = Leilao("Celular")

    # o padrão para o python testar é que o metodo começe com o nome teste_nome_do_metodo
    def test_deve_verificar_o_maior_e_o_menor_lance(self):
        yuri = Usuario('Yuri',200)
        lance_yuri = Lance(yuri,140)
        self.leilao.propoe(self.lance_gui)
        self.leilao.propoe(lance_yuri)
        menor_valor_esperado = 100.0
        maior_valor_esperado = 140.0

        self.assertEqual(menor_valor_esperado,self.leilao.menor_lance) #verifica a igualdade
        self.assertEqual(maior_valor_esperado,self.leilao.maior_lance) #verifica a igualdade

    def test_nao_deve_permitir_que_o_mesmo_usuario_proponha_um_lance_seguido(self):
        lance_gui200 = Lance(self.gui,200)
        with self.assertRaises(ValueError):#aqui estou esperando receber uma exceção , caso contrario o teste falha
            self.leilao.propoe(self.lance_gui)
            self.leilao.propoe(lance_gui200)

        '''
        outra forma de fazer só que pior 
        lance_gui200 = Lance(self.gui,200)
        try:
            self.leilao.propoe(self.lance_gui)
            self.leilao.propoe(lance_gui200)
            self.fail(msg = "Não lançou exceção") #isso garante que vai falhar mesmo que não lance a exceção
                                                  #pois pela regra do negocio era pra ter dado uma exceção
        except ValueError:
            quantidade_de_lances = len(self.leilao.lances)
            self.assertEqual(1,quantidade_de_lances)
        '''